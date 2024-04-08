# home.py
import streamlit as st
from PIL import Image

def app():
    st.sidebar.title("User")
    if st.session_state.get('logged_in', False):
        st.sidebar.write(f"Logged in as: {st.session_state.username}")

    st.markdown("<h1 style='text-align: center;'>Welcome to <span style='color : violet'>FindMyCollege</span></h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    image = Image.open('home_bg.png')
    st.image(image, '')
# home.py
# import streamlit as st
# from PIL import Image
# from session_state import get_session_state

# def app():
#     session_state = get_session_state()

#     st.sidebar.title("User")
#     if session_state.logged_in:
#         st.sidebar.write(f"Logged in as: {session_state.username}")

#     st.markdown("<h1 style='text-align: center;'>Welcome to <span style='color : violet'>FindMyCollege</span></h1>", unsafe_allow_html=True)
#     st.markdown("<br>", unsafe_allow_html=True)
#     image = Image.open('cap-bg.png')
#     st.image(image, '')


