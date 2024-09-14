# File: calculators/retirement_calculator.py

import streamlit as st
import numpy as np
import numpy_financial as npf
from utils.graph_utils import plot_retirement_projection

def retirement_calculator():
    st.header("Retirement Savings Calculator")
    
    # Inputs for retirement projection
    current_savings = st.number_input("Current Savings (₹)", min_value=0.0, step=1000.0, value=0.0)
    monthly_contribution = st.number_input("Monthly Contribution (₹)", min_value=0.0, step=100.0, value=0.0)
    annual_rate = st.slider("Annual Return Rate (%)", min_value=0.0, max_value=15.0, value=5.0)
    years_until_retirement = st.slider("Years Until Retirement", min_value=1, max_value=50, value=30)

    # Calculation
    total_months = years_until_retirement * 12
    monthly_rate = (annual_rate / 100) / 12

    # Use numpy_financial's fv function to calculate future value
    retirement_savings = npf.fv(monthly_rate, total_months, -monthly_contribution, -current_savings)
    st.write(f"**Projected Retirement Savings:** ₹{retirement_savings:,.2f}")

    # Retirement savings growth visualization
    months = np.arange(1, total_months + 1)
    growth = [npf.fv(monthly_rate, m, -monthly_contribution, -current_savings) for m in months]
    
    # Call the plotting function
    plot_retirement_projection(months, growth)
