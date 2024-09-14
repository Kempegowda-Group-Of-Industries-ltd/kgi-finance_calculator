# File: calculators/compound_interest_calculator.py

import streamlit as st
import numpy_financial as npf
import numpy as np
from utils.graph_utils import plot_compound_interest

def compound_interest_calculator():
    st.header("Compound Interest Calculator")
    
    # Inputs for compound interest calculation
    principal = st.number_input("Initial Principal", 0.0, step=1000.0)
    rate = st.slider("Annual Interest Rate (%)", 0.0, 15.0, 5.0)
    years = st.slider("Number of Years", 1, 50, 10)
    contributions = st.number_input("Annual Contributions", 0.0, step=100.0)
    
    # Calculation
    total_months = years * 12
    monthly_rate = (rate / 100) / 12
    
    # Future value calculation using numpy_financial's fv function
    future_value = npf.fv(monthly_rate, total_months, -contributions, -principal)
    st.write(f"**Projected Compound Interest Value:** ₹{future_value:,.2f}")
    
    # Generate data for compound interest growth over time
    months = np.arange(1, total_months + 1)
    growth = [npf.fv(monthly_rate, m, -contributions, -principal) for m in months]
    
    # Plot the compound interest growth
    plot_compound_interest(months, growth)
