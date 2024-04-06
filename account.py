# account.py
import streamlit as st

def signup():
    st.sidebar.title("User")
    if st.session_state.get('logged_in', False):
        st.sidebar.write(f"Logged in as: {st.session_state.username}")
        
    st.title("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if password == confirm_password:
            # Save username and password (this is hardcoded for simplicity)
            with open("users.txt", "a") as file:
                file.write(f"{username}:{password}\n")
            st.success("Account created successfully! Please login.")
        else:
            st.error("Passwords do not match.")

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.success("Successfully logged in!")
            # Set session state to indicate user is logged in
            st.session_state.logged_in = True
            st.session_state.username = username  # Store username in session state
            # Redirect to other pages or perform other actions
        else:
            st.error("Invalid username or password")

def authenticate(username, password):
    # Check if username and password are valid (this is hardcoded for simplicity)
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                return True
    return False

def logout():
    st.session_state.logged_in = False
    st.session_state.username = None

def app():
    st.sidebar.title("Account")
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        choice = st.sidebar.radio("Login or Sign Up", ["Login", "Sign Up"])

        if choice == "Login":
            login()
        elif choice == "Sign Up":
            signup()
    else:
        st.write(f"Welcome, {st.session_state.username}!")  # Display username

        if st.button("Logout"):
            logout()
            st.success("Successfully logged out!")
