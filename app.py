import streamlit as st
import numpy as np
import pandas as pd
import numpy_financial as npf
import matplotlib.pyplot as plt

from calculators.loan_calculator import loan_calculator
from calculators.investment_calculator import investment_calculator
from calculators.budget_calculator import budget_calculator
from calculators.retirement_calculator import retirement_calculator
from calculators.mortgage_calculator import mortgage_calculator
from calculators.auto_loan_calculator import auto_loan_calculator
from calculators.compound_interest_calculator import compound_interest_calculator

# Sidebar for navigation
st.sidebar.title("Finance Calculators & Simulators")
option = st.sidebar.selectbox("Choose a calculator:", 
                             ["Loan Calculator", 
                              "Investment Growth", 
                              "Budget Tracker", 
                              "Retirement Calculator",
                              "Mortgage Calculator",
                              "Auto Loan Calculator",
                              "Compound Interest Calculator"])

# Render the appropriate calculator based on user selection
if option == "Loan Calculator":
    loan_calculator()
elif option == "Investment Growth":
    investment_calculator()
elif option == "Budget Tracker":
    budget_calculator()
elif option == "Retirement Calculator":
    retirement_calculator()
elif option == "Mortgage Calculator":
    mortgage_calculator()
elif option == "Auto Loan Calculator":
    auto_loan_calculator()
elif option == "Compound Interest Calculator":
    compound_interest_calculator()
