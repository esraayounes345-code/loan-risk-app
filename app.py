import streamlit as st
import pandas as pd

st.title("Loan Risk App")

# نشوف أسماء الأعمدة
df = pd.read_csv("ML_Result.csv")
st.write("Columns:", df.columns.tolist())
st.write("First row:", df.head(1))
