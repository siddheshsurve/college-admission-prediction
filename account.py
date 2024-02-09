import streamlit as st

def app():
    st.title("Welcome to :violet[FindMyCollege] 🤩")

    choice = st.selectbox('Login(Already Have Account) / Signup(New User)', ['Login', 'Sign Up'])

    if choice == 'Login':
        st.text_input('Email : ')
        st.text_input('Password : ', type='password')
        st.button('Login')

    else :
        st.text_input('Email : ')
        username = st.text_input('Username : ')
        password = st.text_input('Password : ', type='password')
        st.button('Create Account')