import streamlit as st
import pickle
import pandas as pd

# تحميل الموديل
model = pickle.load(open("loan_model.pkl", "rb"))

st.title("Loan Risk App")

# إدخال البيانات
age = st.number_input("Age")
income = st.number_input("Income")
credit_score = st.number_input("Credit Score")
employment_years = st.number_input("Employment Years")
loan_amount = st.number_input("Loan Amount")
interest_rate = st.number_input("Interest Rate")

# زر التنبؤ
if st.button("Predict"):

    data = pd.DataFrame([{
        "Age": age,
        "Annual_Income": income,
        "Credit_Score": credit_score,
        "Employment_Years": employment_years,
        "Loan_Amount": loan_amount,
        "Loan_Interest_Rate": interest_rate
    }])

    prediction = model.predict(data)

    st.write("Prediction:", prediction[0])
