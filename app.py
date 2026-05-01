import streamlit as st
import pickle
import pandas as pd

# تحميل الموديل
model = pickle.load(open("loan_model.pkl", "rb"))

# عنوان التطبيق
st.title("Loan Risk App")

# إدخال البيانات
age = st.number_input("Age")
income = st.number_input("Income")

# زر التنبؤ
if st.button("Predict"):
    data = pd.DataFrame([[age, income]])
    prediction = model.predict(data)

    st.write("Prediction:", prediction[0])
