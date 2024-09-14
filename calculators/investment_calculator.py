import streamlit as st
import numpy as np
import numpy_financial as npf  # Import the correct library
import matplotlib.pyplot as plt
from utils.graph_utils import plot_investment_growth

def investment_calculator():
    st.header("Investment Growth Calculator")
    
    # Inputs for investment growth projection
    initial_investment = st.number_input("Initial Investment Amount", 0.0, step=1000.0)
    monthly_contribution = st.number_input("Monthly Contribution", 0.0, step=100.0)
    annual_rate = st.slider("Annual Interest Rate (%)", 0.0, 20.0, 7.0)
    years = st.slider("Investment Period (Years)", 1, 50, 20)

    # Calculations
    total_months = years * 12
    monthly_rate = (annual_rate / 100) / 12

    # Use numpy_financial's fv function
    future_value = npf.fv(monthly_rate, total_months, -monthly_contribution, -initial_investment)
    st.write(f"**Projected Future Value:** ₹{future_value:,.2f}")

    # Visualizing Investment Growth
    months = np.arange(1, total_months + 1)
    growth = [npf.fv(monthly_rate, m, -monthly_contribution, -initial_investment) for m in months]
    
    plot_investment_growth(months, growth)
