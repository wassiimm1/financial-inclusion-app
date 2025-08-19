import streamlit as st
import numpy as np
import pickle

# Load model + scaler
randforst = pickle.load(open('randforst.pkl', "rb"))
standardscale = pickle.load(open("standardscale.pkl", "rb"))

st.title("FINANCIAL INCLUSION PREDICTION")

# Inputs
feature1 = st.number_input("INSERT YOUR YEAR OF INTERVIEW")
feature2 = st.number_input("HOW MUCH IS YOUR HOUSE HOLD SIZE")
feature3 = st.number_input("INSERT YOUR AGE")

# Relationship with family head
feature4 = st.radio("SELECT YOUR RELATION WITH FAMILY HEAD:", 
    ('Head of Household', 'Parent', 'Spouse', 'Child', 'Other relative', 'Other non-relatives'))
relationship_mapping = {
    'Head of Household': 6,
    'Parent': 5,
    'Spouse': 4,
    'Child': 3,
    'Other relative': 2,
    'Other non-relatives': 1
}
feature4 = relationship_mapping[feature4]

# Marital status
feature5 = st.radio("SELECT YOUR MARITAL STATUS:", 
    ('Married/Living together', 'Divorced/Seperated', 'Widowed', 'Single/Never Married', 'Dont know'))
marital_mapping = {
    'Married/Living together': 4,
    'Divorced/Seperated': 3,
    'Widowed': 2,
    'Single/Never Married': 1,
    'Dont know': 0
}
feature5 = marital_mapping[feature5]

# Education level
feature6 = st.radio("SELECT YOUR EDUCATION LEVEL:", 
    ('Vocational/Specialised training', 'Tertiary education', 'Secondary education', 'Primary education', 'No formal education', 'Other/Dont know/RTA'))
education_mapping = {
    'Vocational/Specialised training': 5,
    'Tertiary education': 4,
    'Secondary education': 3,
    'Primary education': 2,
    'No formal education': 1,
    'Other/Dont know/RTA': 0
}
feature6 = education_mapping[feature6]

# Country
country = st.radio("SELECT COUNTRY:", ('Kenya', 'Rwanda', 'Tanzania', 'Uganda'))
country_Kenya = int(country == 'Kenya')
country_Rwanda = int(country == 'Rwanda')
country_Tanzania = int(country == 'Tanzania')
country_Uganda = int(country == 'Uganda')

# Location type
location_type = st.radio("SELECT LOCATION TYPE:", ('Rural', 'Urban'))
location_type_Rural = int(location_type == 'Rural')
location_type_Urban = int(location_type == 'Urban')

# Cellphone access
cellphone_access = st.radio("DO YOU HAVE CELLPHONE ACCESS:", ('No', 'Yes'))
cellphone_access_No = int(cellphone_access == 'No')
cellphone_access_Yes = int(cellphone_access == 'Yes')

# Gender
gender_of_respondent = st.radio("SELECT YOUR GENDER:", ('Female', 'Male'))
gender_of_respondent_Female = int(gender_of_respondent == 'Female')
gender_of_respondent_Male = int(gender_of_respondent == 'Male')

# Job type
job_type = st.radio("SELECT YOUR JOB TITLE:", 
    ('Dont Know/Refuse to answer', 'Farming and Fishing', 'Formally employed Government', 
     'Formally employed Private', 'Government Dependent', 'Informally employed', 'No Income', 
     'Other Income', 'Remittance Dependent', 'Self employed'))

job_type_Dont_Know_Refuse_to_answer = int(job_type == 'Dont Know/Refuse to answer')
job_type_Farming_and_Fishing = int(job_type == 'Farming and Fishing')
job_type_Formally_employed_Government = int(job_type == 'Formally employed Government')
job_type_Formally_employed_Private = int(job_type == 'Formally employed Private')
job_type_Government_Dependent = int(job_type == 'Government Dependent')
job_type_Informally_employed = int(job_type == 'Informally employed')
job_type_No_Income = int(job_type == 'No Income')
job_type_Other_Income = int(job_type == 'Other Income')
job_type_Remittance_Dependent = int(job_type == 'Remittance Dependent')
job_type_Self_employed = int(job_type == 'Self employed')

# Prediction
if st.button("Predict"):
    features = np.array([[feature1, feature2, feature3, feature4, feature5, feature6,
                          country_Kenya, country_Rwanda, country_Tanzania, country_Uganda,
                          location_type_Rural, location_type_Urban,
                          cellphone_access_No, cellphone_access_Yes,
                          gender_of_respondent_Female, gender_of_respondent_Male,
                          job_type_Dont_Know_Refuse_to_answer, job_type_Farming_and_Fishing,
                          job_type_Formally_employed_Government, job_type_Formally_employed_Private,
                          job_type_Government_Dependent, job_type_Informally_employed,
                          job_type_No_Income, job_type_Other_Income,
                          job_type_Remittance_Dependent, job_type_Self_employed]])

    features_scaled = standardscale.transform(features)
    prediction = randforst.predict(features_scaled)

    if prediction[0] == 1:
        st.success("✅ You are likely to have a bank account")
    else:
        st.error("❌ You probably don’t have a bank account")
