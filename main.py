import streamlit as st 
from streamlit_option_menu import option_menu

import statistics, account, home, predict_college, contact

st.set_page_config(
    page_title = "FindMyCollege - College Admission Predictor",
    page_icon= "fevicon_main.png"
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title" : title,
            "function" : function
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title = 'FindMyCollege',
                options = ['Home', 'Account', 'Predict College', 'Statistics', 'Contact Us'],
                # icons = ['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                # icons = ['house-fill', 'person-circle', 'clipboard-data-fill', 'info-circle-fill', 'file-person-fill'],
                icons = ['house-fill', 'person-circle', 'clipboard-data-fill', 'bi-graph-up', 'file-person-fill'],
                # menu_icon = 'chat-text-fill',
                menu_icon = 'search-heart-fill',
                default_index = 1,
                styles = {
                    "container" : {
                        "padding" : "5!important", "background-color": "black"
                    },
                    "icon" : {
                        "color" : "white", "font-size": "23px"
                    },
                    "nav-link" : {
                        "color" : "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"
                    },
                    "nav-link-selected" : {
                        "background-color": "#02ab21"
                    },
                }
            )

        if app == "Home":
            home.app()
        if app == "Account":
            account.app()
        if app == "Predict College":
            predict_college.app()
        # if app == "Your Posts":
        #     your_posts.app()
        if app == "Statistics":
            statistics.app()
        if app == "Contact Us":
            contact.app()
    
    run()