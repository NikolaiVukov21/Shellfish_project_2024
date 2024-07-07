import streamlit as st
st.set_page_config(
    page_title="OddAI",
    page_icon="👋",
)

from dep import *

def insert_user(name, password):
    run_sql(f"INSERT INTO people (Username, Password, Time_Created) VALUES ('{name}', '{password}', CURRENT_TIMESTAMP );")
    st.write('Account created!')
    return name

def add_user(name, password, new_user):
    '''
    Returns: name if query is successful, False if not
    '''
    if not password:
        return False
    res = run_sql(f"SELECT Username, Password FROM people WHERE Username = '{name}'")
    # st.write(res)
    if res:
        res_val = res[-1]
        if new_user:
            if res_val['Password'] == password:
                st.write('Signed in!')
                return name
            else:
                st.write('User with this name already exists.')
                return False
        else:
            if res_val['Password'] == password:
                st.write('Signed in!')
                return name
            else:
                st.write('Wrong password. Please try again.')
                return False
    elif not res:
        if not new_user:
            st.write(f"User is not in database. Please make a new account.")
            return False
        else:
            return insert_user(name, password)

st.write('# Sign in to access your files')
new_user = st.checkbox("Create Account", value=False)

if 'user' not in st.session_state:
    st.session_state['user'] = 'Guest'

user = st.text_input("Username", "")
pwd = st.text_input("Password", "")
st.session_state.user = "Guest"

success = add_user(user, pwd, new_user)
if success:
    st.session_state.user = success
