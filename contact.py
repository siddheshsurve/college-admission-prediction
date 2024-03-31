import streamlit as st 
import pandas as pd
def app() :
    # st.title("Contact Us")

    # st.text('Call us on : 8390344586 / 9850365380 / 9730448100')
    # st.text('Mail us at : sysurve24@gmail.com / srtekade2797@gmail.com / tandalesamarth@gmail.com')

    st.title("Contact Us")

    st.title("Contact Us")

    # Developer 1 and 2
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Developer 1")
        st.markdown("**Name:** Siddhesh Surve")
        st.markdown("**Email:** [sysurve24@gmail.com](mailto:sysurve24@gmail.com)")
        st.markdown("**Contact Number:** +91 83903 44586")
        st.markdown("**College Name:** Pune Institute of Computer Technology")

    with col2:
        st.header("Developer 2")
        st.markdown("**Name:** Jane Smith")
        st.markdown("**Email:** [srtekade2797@gmail.com](mailto:srtekade2797@gmail.com)")
        st.markdown("**Contact Number:** +91 98503 65380")
        st.markdown("**College Name:** Pune Institute of Computer Technology")

    # Developer 3 and 4
    col3, col4 = st.columns(2)

    with col3:
        st.header("Developer 3")
        st.markdown("**Name:** Alice Johnson")
        st.markdown("**Email:** [tandalesamarth@gmail.com](mailto:tandalesamarth@gmail.com)")
        st.markdown("**Contact Number:** +91 97304 48100")
        st.markdown("**College Name:** Pune Institute of Computer Technology")

    with col4:
        st.header("Developer 4")
        st.markdown("**Name:** Bob Brown")
        st.markdown("**Email:** [mnarnaware17@gmail.com](mailto:mnarnaware17@gmail.com)")
        st.markdown("**Contact Number:** +91 90214 58965")
        st.markdown("**College Name:** Pune Institute of Computer Technology")

