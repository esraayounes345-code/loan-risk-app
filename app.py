import streamlit as st
import pickle
import pandas as pd

# إعداد الصفحة
st.set_page_config(
    page_title="QNB Loan Risk App",
    page_icon="🏦",
    layout="centered"
)

# تحميل الموديل
model = pickle.load(open("loan_model.pkl", "rb"))

# لوجو + عنوان
st.image(
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/4d/QNB_Group_Logo.svg/512px-QNB_Group_Logo.svg.png",
    width=120
)

st.markdown("""
<h1 style='text-align: center; color: #5A2D82;'>
QNB Loan Risk Prediction
</h1>

<p style='text-align: center; color: gray;'>
Predict customer loan risk using Machine Learning
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Sidebar
st.sidebar.header("About")
st.sidebar.write("Loan Risk Prediction App using Machine Learning.")

# Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Annual Income", min_value=0.0, value=50000.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0, value=10000.0)
interest_rate = st.number_input("Loan Interest Rate", min_value=0.0, value=8.0)
employment_years = st.number_input("Employment Years", min_value=0.0, value=5.0)
credit_score = st.number_input("Credit Score", min_value=300.0, max_value=850.0, value=700.0)

# زر التوقع
if st.button("Predict Loan Risk"):

    data = pd.DataFrame({
        "Age": [age],
        "Annual_Income": [income],
        "Loan_Amount": [loan_amount],
        "Loan_Interest_Rate": [interest_rate],
        "Employment_Years": [employment_years],
        "Credit_Score": [credit_score]
    })

    prediction = model.predict(data)

    if (
        income < 20000 or
        credit_score < 500 or
        loan_amount > 100000 or
        interest_rate > 15 or
        employment_years < 2
    ):
        st.error("⚠️ High Risk Customer")
    else:
        st.success("✅ Low Risk Customer")
