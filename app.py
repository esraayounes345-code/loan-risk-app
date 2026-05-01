import streamlit as st
import pickle

model = pickle.load(open("loan_model.pkl", "rb"))

st.title("Loan Risk App")

age = st.number_input("Age")
income = st.number_input("Income")

st.write(model.feature_names_in_)

if st.button("Predict"):
    st.write("App works successfully")
