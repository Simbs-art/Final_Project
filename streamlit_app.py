import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

# Load model, scaler, encoder, and training features
model = joblib.load('best_random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')
X_train = joblib.load('background_df.pkl')
feature_columns = joblib.load('feature_columns.pkl')

# Streamlit UI
st.set_page_config(page_title="Absenteeism Classifier", layout="centered")
st.title("Employee Absenteeism Predictor")
st.markdown("This app predicts if an employee's absenteeism is **High** or **Low** based on input features.")

# Input form
with st.form("prediction_form"):
    st.subheader("Enter Employee Info")
    distance = st.slider("Distance from Residence to Work (km)", 1, 60, 10)
    transport_expense = st.number_input("Transportation Expense (EUR)", min_value=0, value=200)
    reason_group = st.selectbox("Reason for Absence Group", options=[0, 1, 2, 3], format_func=lambda x: f"Group {x}")
    season = st.selectbox("Season", [1, 2, 3, 4], format_func=lambda x: ["Spring", "Summer", "Fall", "Winter"][x-1])

    submitted = st.form_submit_button("Predict Absenteeism")

if submitted:
    # Create input DataFrame
    input_df = pd.DataFrame({
        'Distance from Residence to Work': [distance],
        'Transportation expense': [transport_expense],
        'Reason group': [reason_group],
        'Seasons': [season]
    })
    input_df = input_df.reindex(columns=feature_columns, fill_value=0) 
    # Scale input and retain column names
    input_scaled_array = scaler.transform(input_df)
    input_scaled = pd.DataFrame(input_scaled_array, columns=input_df.columns)

    # Predict
    pred_numeric = model.predict(input_scaled)[0]
    pred_label = label_encoder.inverse_transform([pred_numeric])[0]

    st.subheader("Prediction Result")
    st.success(f"Predicted Absenteeism Level: **{pred_label}**")

