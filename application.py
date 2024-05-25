import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_model import CustomData, PredictPipeline

# Mapping for user-visible values to backend values
gender_mapping = {"Male": "male", "Female": "female"}
ethnicity_mapping = {"Group A": "group A", "Group B": "group B", "Group C": "group C", "Group D": "group D", "Group E": "group E"}
parental_education_mapping = {"Some High School": "some high school", "High School": "high school", "Some College": "some college", "Associate's Degree": "associate's degree", "Bachelor's Degree": "bachelor's degree", "Master's Degree": "master's degree"}
lunch_mapping = {"Standard": "standard", "Free/Reduced": "free/reduced"}
test_prep_course_mapping = {"Completed": "completed", "None": "none"}

# Define the main function for Streamlit
def main():
    st.title("Student Performance Predictor")
    predict_data_page()

# Function to display the predict data page
def predict_data_page():
    st.header("Predict Student Performance")

    # Display dropdowns with user-visible values
    gender = st.selectbox("Gender", list(gender_mapping.keys()), index=1)
    ethnicity = st.selectbox("Race/Ethnicity", list(ethnicity_mapping.keys()), index=2)
    parental_education = st.selectbox("Parental Education", list(parental_education_mapping.keys()), index=3)
    lunch = st.selectbox("Lunch", list(lunch_mapping.keys()), index=1)
    test_prep_course = st.selectbox("Test Preparation Course", list(test_prep_course_mapping.keys()), index=1)
    reading_score = st.slider("Reading Score", min_value=0, max_value=100, step=1)
    writing_score = st.slider("Writing Score", min_value=0, max_value=100, step=1)

    if st.button("Predict"):
        # Map user-visible values to backend values
        gender_backend = gender_mapping[gender]
        ethnicity_backend = ethnicity_mapping[ethnicity]
        parental_education_backend = parental_education_mapping[parental_education]
        lunch_backend = lunch_mapping[lunch]
        test_prep_course_backend = test_prep_course_mapping[test_prep_course]

        data = CustomData(
            gender=gender_backend,
            race_ethnicity=ethnicity_backend,
            parental_level_of_education=parental_education_backend,
            lunch=lunch_backend,
            test_preparation_course=test_prep_course_backend,
            reading_score=reading_score,
            writing_score=writing_score
        )
        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        st.success(f"Predicted Result: {results[0]}")

# Entry point
if __name__ == '__main__':
    main()
