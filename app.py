import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("loan_model.pkl", "rb"))

st.title("Loan Risk App")

age = st.number_input("Age")
income = st.number_input("Income")

if st.button("Predict"):
    data = pd.DataFrame([[age, income]], columns=["Age", "Income"])
    prediction = model.predict(data)

    st.write("Prediction:", prediction[0])
