import streamlit as st
import numpy_financial as npf

def mortgage_calculator():
    st.header("Mortgage Calculator")
    
    # Input fields
    loan_amount = st.number_input("Mortgage Amount", value=200000, step=1000)
    interest_rate = st.slider("Interest Rate (%)", 0.0, 20.0, 3.5)
    term_years = st.slider("Term (Years)", 1, 30, 15)

    # Monthly interest rate and number of payments
    monthly_rate = (interest_rate / 100) / 12
    num_payments = term_years * 12

    # Monthly payment calculation using numpy_financial's pmt function
    monthly_payment = npf.pmt(monthly_rate, num_payments, loan_amount)

    # Output
    st.write(f"**Monthly Mortgage Payment:** ₹{abs(monthly_payment):,.2f}")
