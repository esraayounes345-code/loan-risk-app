import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("loan_model.pkl", "rb"))

st.title("Loan Risk App")

age = st.number_input("Age")
income = st.number_input("Annual Income")
loan_amount = st.number_input("Loan Amount")
interest_rate = st.number_input("Loan Interest Rate")
employment_years = st.number_input("Employment Years")
credit_score = st.number_input("Credit Score")

if st.button("Predict"):

    data = pd.DataFrame({
        "Age": [age],
        "Annual_Income": [income],
        "Loan_Amount": [loan_amount],
        "Loan_Interest_Rate": [interest_rate],
        "Employment_Years": [employment_years],
        "Credit_Score": [credit_score]
    })

    prediction = model.predict(data)

    st.write("Prediction:", prediction[0])
