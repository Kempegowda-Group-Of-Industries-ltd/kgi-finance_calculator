import numpy as np
import pandas as pd
import streamlit as st
from utils.graph_utils import plot_auto_loan_amortization

def auto_loan_calculator():
    st.header("Auto Loan Calculator")
    
    loan_amount = st.number_input("Loan Amount", 500000.0, step=10000.0)
    annual_rate = st.slider("Annual Interest Rate (%)", 0.0, 15.0, 7.0)
    years = st.slider("Loan Term (Years)", 1, 7, 5)
    
    total_months = years * 12
    monthly_rate = (annual_rate / 100) / 12
    
    # Calculate amortization details
    monthly_payment = np.pmt(monthly_rate, total_months, -loan_amount)
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
    
    # Plot the amortization schedule
    plot_auto_loan_amortization(months, remaining_balance, principal_paid, interest_paid)
