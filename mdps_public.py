# -*- coding: utf-8 -*-
"""
Created on Sun May 8, 2022

@author: siddhardhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    st.header("🔍 Disease Prediction System")
    selected = option_menu(
        "Select Disease Prediction",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
        icons=["activity", "heart", "person"],
        default_index=0,
        menu_icon="stethoscope",
    )

# Custom styling
st.markdown(
    """
    <style>
        .stButton>button {
            color: #fff;
            background-color: #007ACC;
            border-radius: 5px;
            margin-top: 15px;
        }
        .stTextInput>div>div>input {
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to improve column layout and labels
def create_input_form(labels):
    cols = st.columns(len(labels))
    values = [cols[i].text_input(labels[i]) for i in range(len(labels))]
    return values

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.markdown("## Diabetes Prediction using Machine Learning")
    st.markdown("Enter the following details to predict diabetes risk:")

    labels = [
        "Number of Pregnancies", "Glucose Level", "Blood Pressure", "Skin Thickness",
        "Insulin Level", "BMI", "Diabetes Pedigree Function", "Age"
    ]
    values = create_input_form(labels)
    
    # Prediction Button
    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict([values])
        result = "The person is diabetic" if diab_prediction[0] == 1 else "The person is not diabetic"
        st.success(result)

# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":
    st.markdown("## Heart Disease Prediction using Machine Learning")
    st.markdown("Enter the following details to predict heart disease risk:")

    labels = [
        "Age", "Sex", "Chest Pain Type", "Resting Blood Pressure", "Serum Cholesterol (mg/dl)",
        "Fasting Blood Sugar (> 120 mg/dl)", "Resting Electrocardiographic Results", "Max Heart Rate",
        "Exercise Induced Angina", "ST Depression (exercise)", "Peak Exercise ST Segment Slope",
        "Major Vessels by Flouroscopy", "Thalassemia Type (0 = normal; 1 = fixed defect; 2 = reversible defect)"
    ]
    values = create_input_form(labels)
    
    # Prediction Button
    if st.button("Heart Disease Test Result"):
        heart_prediction = heart_disease_model.predict([values])
        result = "The person has heart disease" if heart_prediction[0] == 1 else "The person does not have heart disease"
        st.success(result)

# Parkinson's Prediction Page
if selected == "Parkinson's Prediction":
    st.markdown("## Parkinson's Disease Prediction using Machine Learning")
    st.markdown("Enter the following details to predict Parkinson's disease risk:")

    labels = [
        "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", 
        "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)", 
        "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", 
        "HNR", "RPDE", "DFA", "Spread1", "Spread2", "D2", "PPE"
    ]
    values = create_input_form(labels)
    
    # Prediction Button
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([values])
        result = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(result)
