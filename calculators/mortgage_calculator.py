# File: calculators/mortgage_calculator.py

import streamlit as st
import numpy as np
import numpy_financial as npf
import pandas as pd  # Import pandas
from utils.graph_utils import plot_amortization_schedule

def mortgage_calculator():
    st.header("Mortgage Calculator")
    
    # Input fields
    loan_amount = st.number_input("Loan Amount", 0.0, step=1000.0)
    annual_rate = st.slider("Annual Interest Rate (%)", 0.0, 15.0, 5.0)
    loan_term_years = st.slider("Loan Term (years)", 1, 30, 15)
    
    # Calculation
    total_months = loan_term_years * 12
    monthly_rate = (annual_rate / 100) / 12
    
    # Calculate the monthly payment using numpy_financial
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
    
    # Create a data dictionary and use pandas DataFrame
    data = {
        "Month": months,
        "Remaining Balance": remaining_balance,
        "Principal Paid": principal_paid,
        "Interest Paid": interest_paid
    }
    
    # Convert the data into a DataFrame
    df = pd.DataFrame(data)
    st.write(df)
    
    # Plot the amortization schedule
    plot_amortization_schedule(df)
