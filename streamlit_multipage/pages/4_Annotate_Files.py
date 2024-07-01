
from dep import *

st.write("User:", st.session_state.user)
# st.set_page_config(page_title="Mapping Demo", page_icon="🌍")
all_user_photos = get_photos(st.session_state.user)
if all_user_photos:

    cur_file = kv_select(all_user_photos, 'What file would you like to annotate?')

    # st.write('You selected:', cur_file)

    cur_model = kv_select(get_models(st.session_state.user), 'What model would you like to annotate with?')


    # st.write('You selected:', cur_model)

    val = st.button(label="Annotate")
    if val:
        # print("Button pressed")
        id_ann_img = ann_img(cur_file, cur_model)
        fpath_ann = get_fpath_ann(id_ann_img)
        im = Image.open(fpath_ann)
        st.image(im)
else:
    st.write(f"No annotating files are available to user {st.session_state.user}. Please go to the \"Upload Files\" tab first.")