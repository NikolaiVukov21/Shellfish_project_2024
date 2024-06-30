import streamlit as st
from dep import *
import io
import PIL.Image as Image

# if 'user' not in st.session_state:
#     print("Lost variable")
#     st.session_state['user'] = 'a'

st.write("User:", st.session_state.user)

st.write("Upload files here")

# st.write("User:", st.session_state.user)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    type_file = uploaded_file.type.rsplit('/')[0]
    # print(uploaded_file)
    if type_file == 'image':
        fname = uploaded_file.name
        # print('Here')
        img = Image.open(io.BytesIO(uploaded_file.getvalue()))

        # img.show()
        st.image(img, caption = "Uploaded image")
        st.session_state.raw_photo_id =  add_photo(st.session_state.user, img, fname)
        st.write(f"Added photo with ID = {st.session_state.raw_photo_id}")


        

