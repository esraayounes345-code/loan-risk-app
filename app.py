import streamlit as st
import pickle
import pandas as pd

# إعداد الصفحة
st.set_page_config(
    page_title="QNB Elite Loan Risk",
    page_icon="🏦",
    layout="wide"
)

# تحميل الموديل
model = pickle.load(open("loan_model.pkl", "rb"))

# تصميم احترافي
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #12071f, #2e1065, #0f172a);
}

[data-testid="stHeader"] {
    background: transparent;
}

.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    background: linear-gradient(to right, #ffffff, #d8b4fe, #facc15);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    color: #d1d5db;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
    border-radius: 25px;
    padding: 35px;
    box-shadow: 0px 10px 40px rgba(0,0,0,0.4);
    border: 1px solid rgba(255,255,255,0.1);
}

.stButton>button {
    background: linear-gradient(to right, #7c3aed, #facc15);
    color: black;
    font-size: 20px;
    font-weight: bold;
    border-radius: 18px;
    width: 100%;
    height: 60px;
    border: none;
}

.stButton>button:hover {
    box-shadow: 0px 0px 20px rgba(250,204,21,0.6);
}

.result-box {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    padding: 20px;
    border-radius: 20px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# لوجو
st.image(
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/4d/QNB_Group_Logo.svg/512px-QNB_Group_Logo.svg.png",
    width=140
)

# عنوان
st.markdown('<div class="main-title">QNB Elite Loan Risk</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Banking Intelligence System</div>', unsafe_allow_html=True)

# كارت الإدخال
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100)
    income = st.number_input("Annual Income")
    loan_amount = st.number_input("Loan Amount")

with col2:
    interest_rate = st.number_input("Loan Interest Rate")
    employment_years = st.number_input("Employment Years")
    credit_score = st.number_input("Credit Score")

st.markdown('</div>', unsafe_allow_html=True)

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
        st.markdown(
            '<div class="result-box" style="background:#7f1d1d;color:white;">⚠️ High Risk Customer</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="result-box" style="background:#14532d;color:white;">✅ Low Risk Customer</div>',
            unsafe_allow_html=True
        )
