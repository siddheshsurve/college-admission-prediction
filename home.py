import streamlit as st
from PIL import Image

def app():
    # st.title("College Admission Prediction")
    st.markdown("<h1 style='text-align: center;'>Welcome to <span style='color : violet'>FindMyCollege</span></h1>", unsafe_allow_html=True)
    image = Image.open('cap-bg.png')
    st.image(image, '')