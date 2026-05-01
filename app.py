import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

st.title("Loan Risk App")

# ---- تدريب الـ model من البيانات ----
@st.cache_resource
def train_model():
    df = pd.read_csv("ML_Result.csv")
    
    # نظف الأسماء
    df["Risk_Status"] = df["Risk_Status"].str.extract(r'(High Risk|Low Risk)')
    
    X = df[["Age", "Annual_Income", "Loan_Amount", "Loan_Interest_Rate", "Employment_Years", "Credit_Score"]]
    y = df["Risk_Status"]
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    model = RandomForestClassifier(random_state=42)
    model.fit(X_scaled, y)
    
    return model, scaler

model, scaler = train_model()

# ---- الـ UI ----
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
    
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)
    
    st.write("Prediction:", prediction[0])
