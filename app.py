
import streamlit as st

st.title("Loan Risk App")

age = st.number_input("Age")
income = st.number_input("Income")

if st.button("Predict"):
    st.write("App works successfully")
