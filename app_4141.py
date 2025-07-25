# -*- coding: utf-8 -*-
"""app_4141.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gthOXNWpzpE7cRge_EwyFiVOH3HkLcy8
"""

import streamlit as st
import numpy as np
import pickle

# Load the saved model and scaler
model = pickle.load(open('spam_model_5.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Page configuration
st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

# Title and description
st.title("Heart Disease Prediction App")
st.write("Predict the risk of heart disease using basic health metrics.")

# Input section
st.subheader("Enter Patient Details")

age = st.number_input('Age (in years)', min_value=1, max_value=120, value=50)
sex = st.radio('Sex', ('Male', 'Female'))

cp = st.selectbox('Chest Pain Type (cp)', [
    '0 - Typical angina',
    '1 - Atypical angina',
    '2 - Non-anginal pain',
    '3 - Asymptomatic'
])

trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=50, max_value=250, value=120)
chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=100, max_value=600, value=200)
fbs = st.radio('Fasting Blood Sugar > 120 mg/dl (fbs)', ['0 - False', '1 - True'])

restecg = st.selectbox('Resting ECG Results (restecg)', [
    '0 - Normal',
    '1 - ST-T abnormality',
    '2 - Left ventricular hypertrophy'
])

thalach = st.number_input('Max Heart Rate Achieved (thalach)', min_value=60, max_value=250, value=150)
exang = st.radio('Exercise Induced Angina (exang)', ['0 - No', '1 - Yes'])
oldpeak = st.slider('Oldpeak (ST depression)', min_value=0.0, max_value=6.0, value=1.0, step=0.1)

slope = st.selectbox('Slope of ST segment (slope)', [
    '0 - Upsloping',
    '1 - Flat',
    '2 - Downsloping'
])

ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy (ca)', [0, 1, 2, 3])

thal = st.selectbox('Thalassemia (thal)', [
    '1 - Normal',
    '2 - Fixed defect',
    '3 - Reversible defect'
])

# Prepare input for prediction
input_data = np.array([[
    age,
    1 if sex == 'Male' else 0,
    int(cp.split(' ')[0]),
    trestbps,
    chol,
    int(fbs.split(' ')[0]),
    int(restecg.split(' ')[0]),
    thalach,
    int(exang.split(' ')[0]),
    oldpeak,
    int(slope.split(' ')[0]),
    ca,
    int(thal.split(' ')[0])
]])

# Scale the input
scaled_input = scaler.transform(input_data)

# Prediction
if st.button('Predict'):
    prediction = model.predict(scaled_input)
    st.write("---")
    if prediction[0] == 1:
        st.error("Prediction: The person **has** heart disease.")
    else:
        st.success("Prediction: The person **does not have** heart disease.")