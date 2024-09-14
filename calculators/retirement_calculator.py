import streamlit as st
import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
from utils.graph_utils import plot_retirement_projection

def retirement_calculator():
    st.header("Retirement Savings Calculator")
    
    # Inputs for retirement projection
    current_savings = st.number_input("Current Savings", 0.0, step=1000.0)
    monthly_contribution = st.number_input("Monthly Contribution", 0.0, step=100.0)
    annual_rate = st.slider("Annual Return Rate (%)", 0.0, 15.0, 5.0)
    years_until_retirement = st.slider("Years Until Retirement", 1, 50, 30)

    # Calculation
    total_months = years_until_retirement * 12
    monthly_rate = (annual_rate / 100) / 12

    # Use numpy_financial's fv function
    retirement_savings = npf.fv(monthly_rate, total_months, -monthly_contribution, -current_savings)
    st.write(f"**Projected Retirement Savings:** ₹{retirement_savings:,.2f}")

    # Retirement savings growth visualization
    months = np.arange(1, total_months + 1)
    growth = [npf.fv(monthly_rate, m, -monthly_contribution, -current_savings) for m in months]
    
    plot_retirement_projection(months, growth)
