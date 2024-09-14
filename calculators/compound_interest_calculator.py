import streamlit as st
import numpy as np

def compound_interest_calculator():
    st.header("Compound Interest Calculator")

    # Input fields
    principal = st.number_input("Initial Investment", value=1000, step=500)
    annual_rate = st.slider("Annual Interest Rate (%)", 0.0, 20.0, 5.0)
    years = st.slider("Investment Period (Years)", 1, 50, 10)
    compounds_per_year = st.slider("Compounds per Year", 1, 12, 4)

    # Compound interest formula
    future_value = principal * (1 + (annual_rate / 100) / compounds_per_year) ** (compounds_per_year * years)

    # Output
    st.write(f"**Future Value of Investment:** ₹{future_value:,.2f}")
