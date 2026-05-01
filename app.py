import streamlit as st
import pickle
import pandas as pd

# إعداد الصفحة
st.set_page_config(
    page_title="QNB Premium Loan Risk",
    page_icon="🏦",
    layout="wide"
)

# تحميل الموديل
model = pickle.load(open("loan_model.pkl", "rb"))

# CSS احترافي
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #f3f0ff, #ffffff);
}

.main-title {
    text-align: center;
    color: #4B1D74;
    font-size: 48px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #777;
    font-size: 18px;
    margin-bottom: 30px;
}

.input-box {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
}

.stButton>button {
    background: linear-gradient(to right, #4B1D74, #8B5CF6);
    color: white;
    border-radius: 15px;
    height: 55px;
    width: 100%;
    font-size: 20px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(to right, #8B5CF6, #4B1D74);
}

</style>
""", unsafe_allow_html=True)

# Header
st.image(
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/4d/QNB_Group_Logo.svg/512px-QNB_Group_Logo.svg.png",
    width=140
)

st.markdown('<p class="main-title">QNB Premium Loan Risk</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Smart AI Banking Decision System</p>', unsafe_allow_html=True)

# Inputs داخل Box
st.markdown('<div class="input-box">', unsafe_allow_html=True)

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

st.write("")

# Predict
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
