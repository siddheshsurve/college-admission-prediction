import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import joblib


def app():
    st.sidebar.title("User")
    if st.session_state.get('logged_in', False):
        st.sidebar.write(f"Logged in as: {st.session_state.username}")
    
    st.title("College Admission Predictor : \n\n")

    #Loading the trained model
    with open('dt_classifier.pkl', 'rb') as file:
        model = pickle.load(file)
    
    #Loading the label encoders and decoders
    with open('encoded_feat.pkl', 'rb') as file:
        encoded_features = pickle.load(file)
    
    #Loading trained Random Forest model with  
    with open('rfmodel.pkl', 'rb') as file:
        rfmodel = joblib.load(file)


    # model = pickle.load(open('decision_tree_classifier.sav', 'rb'))
    # encoded_features = pickle.load(open('encoded_features.sav', 'rb'))
    

    #Function to encode input data
    def encode_input_data(input_data, mappings):
        encoded_data = input_data.copy()
        for feature in mappings:
            if feature in encoded_data:
                encoded_data[feature] = encoded_data[feature].map(mappings[feature])
        return encoded_data
    
    #Function to decode predictions
    def decode_predictions(encoded_predictions, label_decoder):
        return [list(label_decoder.keys())[list(label_decoder.values()).index(pred)] for pred in encoded_predictions]
    

    #Input form
    st.header('Enter Student Details : ')
    # percentile = st.slider('Percentile', 30.00, 100.00, 50.00)
    percentile = st.number_input('Percentile : ', min_value=30.0, max_value=100.0, value=50.0, step=0.1)
    branch = st.selectbox('Branch', ['computer science and engineering', 'civil engineering', 'electronics and telecommunication engg', 'information technology', 'mechanical engineering'])
    gender = st.selectbox('Gender', ['f', 'm'])
    category = st.selectbox('Category', ['open', 'obc', 'sbc', 'sc', 'st'])
    seat_type = st.selectbox('Secondary Seat Type', ['all india seats allotted to all india candidature candidates with mht-cet score', 'all india seats allotted to all india candidature candidates with jee(main) score', 'home university seats allotted to home university candidates', 'home university seats allotted to other than home university candidates', 'other than home university seats allotted to home university candidates', 'other than home university seats allotted to other than home university candidates', 'state level seats'])
    score_type = st.selectbox('Score Type', ['mht-cet', 'jee(main)', 'merit'])
    city = st.selectbox('City', ['pune', 'mumbai', 'satara', 'thane'])

    #Predict button
    if st.button('Predict'):
        #Create DataFrame from user inputs
        input_data = pd.DataFrame({
            'percentile': [percentile],
            'branch': [branch],
            'gender': [gender],
            'category': [category],
            'secondary_seat_type': [seat_type],
            'score_type': [score_type],
            'city': [city]
        })

        #Encode input data
        encoded_input = encode_input_data(input_data, encoded_features)

        #Make Prediction
        # encoded_predictions = model.predict(encoded_input)
        encoded_predictions = rfmodel.predict(encoded_input)

        #Decode Prediction
        decode_predictions = decode_predictions(encoded_predictions, encoded_features['college_name'])

        #Show predictions
        # st.write('Predicted College Name:', decode_predictions[0].title())

        # Make predictions for the encoded_input_data using trained Random Forest Model
        encoded_predictions_proba_rf = rfmodel.predict_proba(encoded_input)
        top_5_indices_rf = encoded_predictions_proba_rf.argsort()[:, -5:][0]
        top_5_college_labels_rf = [list(encoded_features['college_name'].keys())[idx] for idx in top_5_indices_rf]
        top_5_probabilities_rf = encoded_predictions_proba_rf[0][top_5_indices_rf]
        top_5_probabilities_perc_rf = top_5_probabilities_rf*100

        #Descending order
        top_5_college_labels_rf = top_5_college_labels_rf[::-1]
        top_5_probabilities_perc_rf = top_5_probabilities_perc_rf[::-1]

        top_5_college_labels_rf = [label.title() for label in top_5_college_labels_rf]

        #Display top 5 predicted colleges and their probabilities
        st.write("Top 5 Predicted Colleges and Probabilities:")
        for college, probability in zip(top_5_college_labels_rf, top_5_probabilities_perc_rf):
            st.write(f"- {college}: {probability:.2f}%")

        
        # Create a pie chart 
        fig, ax = plt.subplots(figsize=(25, 25), facecolor='black')
        ax.pie(top_5_probabilities_perc_rf, labels=top_5_college_labels_rf, autopct='%1.1f%%', startangle=90, textprops={'color': 'white', 'fontsize': 25})
        ax.axis('equal')
        plt.title('Top 5 Predicted Colleges\n\n\n', color='white', fontsize=30)
        st.pyplot(fig)



        
