import streamlit as st
import numpy_financial as npf

def auto_loan_calculator():
    st.header("Auto Loan Calculator")
    
    # Input fields
    loan_amount = st.number_input("Auto Loan Amount", value=10000, step=1000)
    interest_rate = st.slider("Interest Rate (%)", 0.0, 20.0, 5.0)
    term_years = st.slider("Term (Years)", 1, 7, 5)

    # Monthly interest rate and number of payments
    monthly_rate = (interest_rate / 100) / 12
    num_payments = term_years * 12

    # Monthly payment calculation using numpy_financial's pmt function
    monthly_payment = npf.pmt(monthly_rate, num_payments, loan_amount)

    # Output
    st.write(f"**Monthly Auto Loan Payment:** ₹{abs(monthly_payment):,.2f}")
