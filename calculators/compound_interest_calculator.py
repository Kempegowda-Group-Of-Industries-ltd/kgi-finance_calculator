import numpy as np
import pandas as pd
import streamlit as st
from utils.graph_utils import plot_compound_interest_growth

def compound_interest_calculator():
    st.header("Compound Interest Calculator")
    
    initial_investment = st.number_input("Initial Investment", 1000.0, step=500.0)
    monthly_contribution = st.number_input("Monthly Contribution", 500.0, step=100.0)
    annual_rate = st.slider("Annual Interest Rate (%)", 0.0, 20.0, 5.0)
    years = st.slider("Investment Period (Years)", 1, 50, 10)

    total_months = years * 12
    monthly_rate = (annual_rate / 100) / 12

    # Compound interest growth calculation
    months = np.arange(1, total_months + 1)
    growth = [np.fv(monthly_rate, m, -monthly_contribution, -initial_investment) for m in months]
    
    # Plot the compound interest growth
    plot_compound_interest_growth(months, growth)
