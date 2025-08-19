import streamlit as st
import pickle

randforst = pickle.load(open('randforst.pkl',"rb"))
standardscale = pickle.load(open("standardscale.pkl","rb"))

st.title("FINANCIAL INCLUSION PREDICTION ")
feature1 = st.number_input("INSERT YOUR YEAR OF INTERVIEW")
feature2 = st.number_input('HOW MUCH IS YOUR HOUSE HOLD SIZE')
feature3 = st.number_input('INSERT YOUR AGE ')
feature4 = st.radio("SELECT YOUR RELATION WITH FAMILY HEAD: ", ('Head of Household', 'Parent','9-12 month','Spouse','Child','Other relative','Other non-relatives'))
relationship_with_head_mapping = {
    'Head of Household':6,
    'Parent': 5,
    'Spouse':4,
    'Child': 3,
    'Other relative': 2,
    'Other non-relatives': 1}
feature4 = relationship_with_head_mapping[feature4]	

feature5 = st.radio("SELECT YOUR MARTIAL STATUS	: ", ('Married/Living together','Divorced/Seperated','Widowed''Single/Never Married','Dont know'))
relationship_with_head_mapping = {
    'Married/Living together':4,
    'Divorced/Seperated': 3,
    'Widowed':2,
    'Single/Never Married': 1,
    'Dont know': 0}
feature5 = relationship_with_head_mapping[feature5]	

feature6 = st.radio("SELECT YOUR EDUCATION LEVEL: ", ('Vocational/Specialised training','Tertiary education','Secondary education','Primary education','No formal education','Other/Dont know/RTA'))
relationship_with_head_mapping = {
    'Vocational/Specialised training':5,
    'Tertiary education':4,
    'Secondary education':3,
    'Primary education': 2,
    'No formal education':1,
    'Other/Dont know/RTA': 0}
feature6 = relationship_with_head_mapping[feature6]	

country = st.radio("SELECT COUNTRY: ", ('Kenya','Rwanda','Tanzania','Uganda'))
country_Kenya = 0
country_Rwanda = 0
country_Tanzania = 0
country_Uganda = 0
if country == 'Kenya':
    country_Kenya = 1
elif country == 'Rwanda':
    country_Rwanda = 1
elif country == 'Tanzania':
    country_Tanzania = 1
elif country == 'Uganda':
    country_Uganda = 1

location_type = st.radio("SELECT LOCATION TYPE: ", ('Rural','Urban'))
location_type_Rural = 0
location_type_Urban = 0
if location_type == 'Rural':
    location_type_Rural = 1
elif location_type == 'Urban':
    location_type_Urban = 1

cellphone_access = st.radio("DO YOU HAVE CELLPHONE ACCESS: ", ('No','Yes'))
cellphone_access_No = 0
cellphone_access_Yes = 0
if cellphone_access == 'No':
    cellphone_access_No = 1
elif cellphone_access == 'Yes':
    cellphone_access_Yes = 1

gender_of_respondent =st.radio("SELECT YOUR GENDER: ", ('Female','Male'))
gender_of_respondent_Female = 0
gender_of_respondent_Male = 0
if gender_of_respondent == 'Female':
    gender_of_respondent_Female = 1
elif gender_of_respondent_Male == 'Male':
    cellphone_access_Yes = 1

job_type =st.radio("SELECT YOUR JOB TITLE: ", ('Dont Know/Refuse to answer','Farming and Fishing','Formally employed Government','Formally employed Private','Government Dependent','Informally employed','No Income','Other Income','Remittance Dependent','Self employed'))
job_type_Dont_Know_Refuse_to_answer = 0
job_type_Farming_and_Fishing = 0
job_type_Formally_employed_Government = 0
job_type_Formally_employed_Private = 0
job_type_Government_Dependent = 0
job_type_Informally_employed = 0
job_type_No_Income = 0
job_type_Other_Income = 0
job_type_Remittance_Dependent = 0
job_type_Self_employed = 0
if job_type == 'KenyDont Know/Refuse to answera':
    job_type_Dont_Know_Refuse_to_answer = 1
elif job_type == 'Farming and Fishing':
    job_type_Farming_and_Fishing = 1
elif job_type == 'Formally employed Government':
    job_type_Formally_employed_Government = 1
elif job_type == 'Formally employed Private':
    job_type_Formally_employed_Private = 1
elif job_type == 'Government Dependent':
    job_type_Government_Dependent = 1  
elif job_type == 'Informally employed':
    job_type_Informally_employed = 1
elif job_type == 'No Income':
    job_type_No_Income = 1
elif job_type == 'Other Income':
    job_type_Other_Income = 1
elif job_type == 'Remittance Dependent':
    job_type_Remittance_Dependent = 1      
elif job_type == 'Self employed':
    job_type_Self_employed = 1

if st.button("Predict"):
    features = np.array([[feature1,feature2,feature3,feature4,feature5,feature6,country_Kenya,country_Rwanda ,country_Tanzania,country_Uganda,location_type_Rural,location_type_Urban,cellphone_access_No,cellphone_access_Yes,gender_of_respondent_Female,gender_of_respondent_Male,job_type_Dont_Know_Refuse_to_answer,job_type_Farming_and_Fishing,job_type_Formally_employed_Government,job_type_Formally_employed_Private,job_type_Government_Dependent,job_type_Informally_employed,job_type_No_Income,job_type_Other_Income,job_type_Remittance_Dependent,job_type_Self_employed]])
    features_scaled = standardscale.transform(features)
    prediction = randforst.predict(features_scaled)
    if prediction[0] == 1:
        st.success("you are likely to have a bank account")
    else :
        st.error('you are probably dont have a bank account')                     