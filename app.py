import streamlit as st
import pandas as pd
import joblib

st.title("ML Classification App")

uploaded_file = st.file_uploader("Upload Test CSV", type=["csv"])

model_choice = st.selectbox("Select Model", [
    "Logistic Regression",
    "Decision Tree",
    "KNN",
    "Naive Bayes",
    "Random Forest",
    "XGBoost"
])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    model = joblib.load(f"model/{model_choice}.pkl")
    predictions = model.predict(data)

    st.write("Predictions:")
    st.write(predictions)
