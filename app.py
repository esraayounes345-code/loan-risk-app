import pandas as pd
import streamlit as st
data = pd.DataFrame([[
    age,
    annual_income,
    credit_score,
    employment_years,
    loan_interest_rate,
    loan_amount
]], columns=[
    "Age",
    "Annual_Income",
    "Credit_Score",
    "Employment_Years",
    "Loan_Interest_Rate",
    "Loan_Amount"
])