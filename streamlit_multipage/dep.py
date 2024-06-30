import pandas as pd
import pymysql
from pymysql.err import IntegrityError, OperationalError
import os
from PIL import Image
import numpy as np
import supervision as sv
import cv2
import av
from PIL import Image
import shutil as sh
import re
from roboflow import Roboflow
import cv2
from ultralytics import YOLOv10
import wget
from time import time
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os
import streamlit as st

temp_folder = os.path.join('.', 'Files_local')
temp_weights = os.path.join(temp_folder, 'Weights')

bba = sv.BoxCornerAnnotator()
la = sv.LabelAnnotator(text_scale = 0.4, text_padding = 1)

db_main = 'test_4'
cur_name = 'ab'

sql_conn = pymysql.connect(
    user="root",
    password="dbuserdbuser",
    host="localhost",
    port=3309,
    database=db_main,
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True)
cur = sql_conn.cursor()


###########################
# GOOGLE HELPER FUNCTIONS #
###########################
import json
def sign_in_storage_g(path_to_cred = '', JSON_file = 'molten-album-427115-q6-cfa4e4aaf3bd.json'):
    f = open(os.path.join(path_to_cred, JSON_file))
    credentials_dict = json.load(f)
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict)
    client = storage.Client(credentials=credentials, project='molten-album-427115-q6')
    bkt = client.get_bucket('test_bucket_abc123')
    print("Connected to google cloud")
    return bkt, client

b, cl = sign_in_storage_g(path_to_cred='../sql/')

def check_folder_exists_g(folder_to_upload, check_location, disable = False, full = False, bkt = b): # assume full installation
    # assumes if one file is in the right location then they all are
    try:
        if disable:
            return True
        cur_path = folder_to_upload
        path_check_exist_g = check_location
        if not os.path.exists(cur_path):
            return False
        all_items = os.listdir(cur_path)
        for added_item in all_items: # searching for a file
            cur_path = os.path.join(cur_path, added_item)
            path_check_exist_g = os.path.join(path_check_exist_g, added_item)
            cur_exists = False
            if os.path.isfile(cur_path): # if you just want to make sure one file is the same, set full to 
                cur_exists = path_exists_g(path_check_exist_g)
                if not full: 
                    return cur_exists
            elif os.path.isdir(cur_path):
                cur_exists = check_folder_exists_g(cur_path, path_check_exist_g)
            if not cur_exists:
                return False
        return True
    except Exception:
        print(f"Current folder {folder_to_upload} or {check_location} is malformed")
        return False

def upload_file_g(file_to_upload, new_name_with_path_g, bkt = b):
    blob = bkt.blob(new_name_with_path_g)
    blob.upload_from_filename(file_to_upload)
    

def upload_folder_g(folder_to_upload, new_name_with_path_g, bkt = b , level = 0, overwrite = False):
    already_uploaded = False
    if level == 0: # check if already uploaded
        already_uploaded = check_folder_exists_g(folder_to_upload, new_name_with_path_g)
        level += 1
    if os.path.exists(folder_to_upload) and (not already_uploaded or overwrite):
        for item in os.listdir(folder_to_upload):
            cur_path = os.path.join(folder_to_upload, item)
            new_path_g = os.path.join(new_name_with_path_g, item)
            if os.path.isfile(cur_path):
                upload_file_g(cur_path, new_path_g)
            elif os.path.isdir(new_path_g):
                upload_folder_g(cur_path, new_path_g, level)

def download_file_g(file_to_download_g, new_name_with_path, bkt = b):
    if not os.path.exists(new_name_with_path):
        blob = bkt.blob(file_to_download_g)
        blob.download_to_filename(new_name_with_path)

def list_blobs_g(folder_base, bkt = b, client = cl):
    """Lists all the blobs in the bucket that begin with the prefix."""
    blobs = bkt.list_blobs(prefix=folder_base)
    return blobs

def download_folder_g(folder_to_download_g, new_name_with_path, overwrite = False, level = 0, file_depth = 3):
    already_uploaded = False
    if level == 0: # check if already downloaded
        already_uploaded = os.path.exists(new_name_with_path)
        level += 1
    if not check_folder_exists_g(new_name_with_path, folder_to_download_g) and (not already_uploaded or overwrite):
        for item in list_blobs_g(folder_to_download_g):
            file_path_g = item.name
            file_name = trim_file_depth(file_path_g, start = file_depth)
            local_path = os.path.join(new_name_with_path, file_name)
            download_file_g(file_path_g, local_path)             


def make_folder_g(folder_name, bkt = b):
    blob = bkt.blob(folder_name + '/')
    blob.upload_from_string('')

def path_exists_g(file, bkt = b):
    blob = bkt.blob(file)
    return blob.exists()
###############################
# LOCAL FILE HELPER FUNCTIONS #
###############################

def get_filename(fpath):
    return fpath.replace('\\', '/').rsplit('/', 1)[-1]

def get_ext(fpath):
    fname = get_filename(fpath)
    per_index = fname.index('.')
    ext = fname[per_index + 1:].lower()
    return ext

def get_id_fname(f_out, fpath, id):
    fname = get_filename(fpath)
    per_index = fname.index('.')
    ext = fname[per_index + 1:].lower()
    return os.path.join(f_out, f"{fname[:per_index]}-{id}.{ext}").replace('\\', '/')

def get_REPLACE_ID(column_id = 'Raw_File_ID', table='raw_files', column_rep='Filepath'):
    cur.execute(f"""SELECT {column_id} from {table} where {column_rep} = 'REPLACE'""")
    id = cur.fetchall()[-1][column_id]
    return id

def get_match(pattern, string):
    matches = re.search(pattern, string)
    if matches:
        print(matches.group(1))
        return(matches.group(1))
    else:
        raise ValueError(f'Improper string exported, couldn\'t find {pattern} in the given text')



def delete_folder(name, base = "."):
    fpath = os.path.join(base, name)
    if os.path.exists(fpath):
        for item in os.listdir(fpath):
            new_path = os.path.join(fpath, item)
            if os.path.isfile(new_path):
                os.remove(new_path)
            elif os.path.isdir(new_path):
                delete_folder(item, fpath)
        os.rmdir(fpath)
                
def make_folder(fpath, overwrite = False):
    delete_folder(fpath, '.') if overwrite else None
    if not os.path.exists(fpath):
        os.mkdir(fpath)
        
def get_temp_fname(fpath, temp_f = temp_folder):
    fname = fpath.replace('\\', '/').rsplit('/', 1)[-1]
    return os.path.join(temp_folder, fname).replace('\\', '/')

def trim_file_depth(fpath, start = 0, end = 'Unused'):
    split_ls = fpath.rsplit('/')
    if end == 'Unused':
        end = len(split_ls)
    return '/'.join(split_ls[start:end])


if not path_exists_g('Files/'):
    make_folder_g('Files')
    make_folder_g('Files/Video_raw')
    make_folder_g('Files/Video_ann')
    make_folder_g('Files/Image_raw')
    make_folder_g('Files/Image_ann')
    make_folder_g('Files/Model')
    make_folder_g('Files/Roboflow')
make_folder(temp_folder)

###########################
# SQL/Database Management #
###########################

def add_user(name, password, new_user):
    '''
    Returns: name if query is successful, False if not
    '''
    if new_user:
        try:
            cur.execute(f"INSERT INTO people (Username, Password, Time_Created) VALUES ('{name}', '{password}', CURRENT_TIMESTAMP );")
        except IntegrityError:
            st.write(f"Duplicate User with {name}. Please try a different username.")
            return False
        st.write("New account created!")
        return name
    else:
        cur.execute(f"SELECT Username, Password FROM people WHERE Username = '{name}'")
        res = cur.fetchall()
        # print(res)
        if not res:
            st.write(f"User is not in database. Please make a new account.")
            return False
        elif res[-1]['Password'] != password:
            st.write(f"Wrong password. Please try again.")
            return False
        else:
            st.write("Signed in!")
            return name


def add_photo(user, im, filename, notes = '', f_out = 'Files/Image_raw'):
    '''
    Returns: Index of added photo if successful, 0 if not
    '''
    # im is a PILLOW image
    width = im.size[0]
    height = im.size[1]
    f_temp = get_temp_fname(filename)
    im.save(f_temp)
    fsize = os.stat(f_temp).st_size
    ext = get_ext(f_temp)
    
    cur.execute(f"INSERT INTO raw_files (Username, Filepath, Filename, Local_Path, Size, Type, Extension, Notes, Width, Height, Time_Uploaded) VALUES ('{user}', 'REPLACE', 'REPLACE', 'REPLACE', {fsize}, 'Image', '{ext}', '{notes}', {width}, {height}, CURRENT_TIMESTAMP);")
    id = get_REPLACE_ID()

    f_id_name_g = get_id_fname(f_out, f_temp, id)
    temp_fname = get_temp_fname(f_id_name_g)
    fname = get_filename(temp_fname)
    # print(temp_fname)
    upload_file_g(f_temp, f_id_name_g)
    cur.execute(f"UPDATE raw_files SET Filepath = '{f_id_name_g}', Local_Path = '{temp_fname}', Filename = '{fname}' WHERE Raw_File_ID = {id};")
    # print(f"\n\n\n\n'{user}', '{f_id_name_g}', '{temp_fname}', {fsize}, 'Image', '{ext}', '{notes}', {width}, {height}")
    return id

def get_photos(user):
    cur.execute(f"SELECT Filepath, Filename, Raw_File_ID FROM raw_files WHERE Username = '{user}';")
    res = cur.fetchall()
    # print("Start of result")
    # print(res)
    # print("End of result")
    keys = [row['Filename'] for row in res]
    values = [row['Raw_File_ID'] for row in res]
    return dict(zip(keys, values))

def get_models():
    cur.execute(f"SELECT Model_ID from models WHERE Model_Points_Path != 'REPLACE';")
    res = cur.fetchall()

    all_mods = [row['Model_ID'] for row in res]

    return all_mods


    # dict(zip([res['Filepath']]))

def annotate_image(input_img, model, label_annotator = la, bounding_box_annotator = bba, verbose = False, conf = True, conf_level = 0.05):
    
    cont_img = np.ascontiguousarray(input_img, dtype=np.uint8)
    results = model(cont_img, conf=conf_level, verbose = verbose)[0]
    conf_array = np.array(results.boxes.conf.cpu())
    conf_ls_str  = [str(round(x * 100) ) + '%' for x in conf_array]
    tot_time = sum([x for x in results.speed.values()])
    
    detections = sv.Detections.from_ultralytics(results)
    annotated_image = bounding_box_annotator.annotate(
        scene=input_img, detections=detections)
    num_oysters = detections.xyxy.shape[0]
    annotated_image = label_annotator.annotate(
        scene=annotated_image, detections=detections, labels = conf_ls_str)
    return(annotated_image, num_oysters, tot_time, detections)

def ann_img(Raw_File_ID, Model_ID, threshold = 0.3, notes = '', f_out = 'Files/Image_ann'):
    cur.execute(f"SELECT * FROM raw_files WHERE Raw_File_ID = {Raw_File_ID}")
    cur_photo = cur.fetchall()[-1]

    cur.execute(f"SELECT * FROM models WHERE Model_ID = {Model_ID}")
    cur_model = cur.fetchall()[-1]

    cur.execute(f"SELECT * from annotated_files WHERE Model_ID = {Model_ID} AND Raw_File_ID = {Raw_File_ID}")
    res = cur.fetchall()
    if res:
        print('Image Already Annotated')
        return res[-1]['Ann_File_ID']
    
    download_file_g(cur_photo['Filepath'], cur_photo['Local_Path'])
    im = Image.open(cur_photo['Local_Path'])
    np_img = np.array(im)

    download_file_g(cur_model['Model_Points_Path'], cur_model['Local_Path'])
    model = YOLOv10(cur_model['Local_Path'])
    annot, num_oysters, tot_time, end_ann_data = annotate_image(np_img, model, conf_level = threshold)

    cur.execute(f"INSERT INTO annotated_files (Raw_File_ID, Model_ID, Annotated_Filepath, Time_to_Annotate, Confidence_Threshold, Notes, Timestamp) VALUES ('{Raw_File_ID}', '{Model_ID}', 'REPLACE', '{tot_time}', {threshold}, '{notes}', CURRENT_TIMESTAMP);")
    id = get_REPLACE_ID(column_id = 'Ann_File_ID', table='annotated_files', column_rep='Annotated_Filepath')
    f_id_name_g = get_id_fname(f_out, cur_photo['Filepath'], id)
    f_local = get_temp_fname(f_id_name_g)
    print(f_local)

    im_f = Image.fromarray(annot)
    im_f.save(f_local)



    upload_file_g(f_local, f_id_name_g)


    cur.execute(f"UPDATE annotated_files SET Annotated_Filepath = '{f_id_name_g}', Local_Path = '{f_local}' WHERE Ann_File_ID = {id};")
    cur.execute(f"INSERT INTO annotated_photos (Ann_File_ID, Number_of_Oysters) VALUES ({id}, {num_oysters})")

    coord = end_ann_data.xyxy
    conf = end_ann_data.confidence
    names = end_ann_data.data['class_name']
    class_num = end_ann_data.class_id
    for idx in range(len(coord)):
        coord_cur = coord[idx]
        cur.execute(f"INSERT INTO oysters_in_photo (Ann_File_ID, Confidence, X1, Y1, X2, Y2, Class, Class_Index) VALUES ({id}, {conf[idx]}, {coord_cur[0]}, {coord_cur[1]}, {coord_cur[2]}, {coord_cur[3]}, '{names[idx]}', {class_num[idx]});")
    return id

def get_fpath_ann(ann_id):
    cur.execute(f"SELECT Local_Path from annotated_files WHERE Ann_File_ID = {ann_id}")
    res = cur.fetchall()
    return res[-1]['Local_Path']
# ann_photo_id = ann_img(id_raw_photo, id_mod)

