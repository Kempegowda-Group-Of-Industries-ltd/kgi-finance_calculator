import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils.graph_utils import plot_amortization_schedule

def loan_calculator():
    st.header("Loan Calculator")
    
    # Input Fields
    loan_amount = st.slider("Loan Amount", 1000, 500000, 100000)
    interest_rate = st.slider("Interest Rate (in %)", 1.0, 15.0, 5.0)
    loan_term = st.slider("Loan Term (in years)", 1, 30, 15)

    # Monthly interest rate and number of payments
    monthly_rate = (interest_rate / 100) / 12
    num_payments = loan_term * 12

    # Monthly payment formula (simple amortization formula)
    monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate)**(-num_payments))

    # Show calculated monthly payment
    st.write(f"**Monthly Payment:** ₹{monthly_payment:,.2f}")

    # Generate amortization schedule
    principal_paid, interest_paid, remaining_balance = [], [], []
    for n in range(1, num_payments + 1):
        interest = loan_amount * monthly_rate
        principal = monthly_payment - interest
        loan_amount -= principal
        principal_paid.append(principal)
        interest_paid.append(interest)
        remaining_balance.append(loan_amount)

    amortization_data = pd.DataFrame({
        "Principal Paid": principal_paid,
        "Interest Paid": interest_paid,
        "Remaining Balance": remaining_balance
    })

    # Plot amortization schedule
    plot_amortization_schedule(amortization_data)
