# -*- coding: utf-8 -*-
"""
Updated for Enhanced UI and Theme Toggle
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_toggle import st_toggle_switch

# loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar for navigation and theme toggle
with st.sidebar:
    st.title("Disease Prediction System")
    selected = option_menu(
        "Choose Prediction Type",
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )
    
    # Theme Toggle
    theme = st_toggle_switch(
        label="Dark Mode",
        key="theme_toggle",
        default_value=False
    )

# Apply Theme Colors
if theme:
    st.markdown(
        """
        <style>
        body {background-color: #1e1e1e; color: white;}
        .stTextInput label {color: #c9c9c9;}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        body {background-color: #f0f2f6; color: black;}
        </style>
        """,
        unsafe_allow_html=True
    )

# Prediction Pages with Improved Layout and Input Validation

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction using ML")
    col1, col2, col3 = st.columns(3)
    
    # Input Fields
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    # Prediction
    diab_diagnosis = ""
    if st.button('Diabetes Test Result'):
        try:
            input_data = [float(Pregnancies), float(Glucose), float(BloodPressure),
                          float(SkinThickness), float(Insulin), float(BMI), 
                          float(DiabetesPedigreeFunction), float(Age)]
            diab_prediction = diabetes_model.predict([input_data])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        except ValueError:
            diab_diagnosis = "Please enter valid numerical values."

    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)
    
    # Input Fields
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1 = Male, 0 = Female)')
    with col3:
        cp = st.text_input('Chest Pain type (0-3)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0, 1, or 2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0-2)')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (0-3)')
    with col1:
        thal = st.text_input('Thal (1 = normal; 2 = fixed defect; 3 = reversible defect)')

    # Prediction
    heart_diagnosis = ""
    if st.button('Heart Disease Test Result'):
        try:
            input_data = [float(age), float(sex), float(cp), float(trestbps), 
                          float(chol), float(fbs), float(restecg), float(thalach), 
                          float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
            heart_prediction = heart_disease_model.predict([input_data])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease'
            else:
                heart_diagnosis = 'The person does not have heart disease'
        except ValueError:
            heart_diagnosis = "Please enter valid numerical values."

    st.success(heart_diagnosis)


# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    cols = st.columns(5)  
    
    # Input Fields
    inputs = [
        "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)",
        "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)",
        "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR",
        "HNR", "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
    ]
    input_values = [cols[i % 5].text_input(inputs[i]) for i in range(len(inputs))]

    # Prediction
    parkinsons_diagnosis = ""
    if st.button("Parkinson's Test Result"):
        try:
            input_data = [float(value) for value in input_values]
            parkinsons_prediction = parkinsons_model.predict([input_data])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
        except ValueError:
            parkinsons_diagnosis = "Please enter valid numerical values."

    st.success(parkinsons_diagnosis)
