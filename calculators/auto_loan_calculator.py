# File: calculators/auto_loan_calculator.py

import streamlit as st
import numpy_financial as npf  # Correct import
import numpy as np
from utils.graph_utils import plot_amortization_schedule

def auto_loan_calculator():
    st.header("Auto Loan Calculator")
    
    # Input fields
    loan_amount = st.number_input("Loan Amount", 0.0, step=1000.0)
    annual_rate = st.slider("Annual Interest Rate (%)", 0.0, 15.0, 5.0)
    loan_term_years = st.slider("Loan Term (years)", 1, 7, 5)
    
    # Calculation
    total_months = loan_term_years * 12
    monthly_rate = (annual_rate / 100) / 12
    
    # Correcting the usage of pmt function with numpy_financial
    monthly_payment = npf.pmt(monthly_rate, total_months, -loan_amount)
    st.write(f"**Monthly Payment:** ₹{monthly_payment:,.2f}")
    
    # Generate data for amortization schedule
    months = np.arange(1, total_months + 1)
    remaining_balance = []
    principal_paid = []
    interest_paid = []
    balance = loan_amount
    
    for month in months:
        interest = balance * monthly_rate
        principal = monthly_payment - interest
        balance -= principal
        remaining_balance.append(balance)
        principal_paid.append(principal)
        interest_paid.append(interest)
    
    # Create a data dictionary for plotting
    data = {
        "Remaining Balance": remaining_balance,
        "Principal Paid": principal_paid,
        "Interest Paid": interest_paid
    }
    
    # Plot amortization schedule
    plot_amortization_schedule(data)
