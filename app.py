import streamlit as st
from calculators.loan_calculator import loan_calculator
from calculators.investment_calculator import investment_calculator
from calculators.budget_calculator import budget_calculator
from calculators.retirement_calculator import retirement_calculator

# Sidebar for navigation
st.sidebar.title("Finance Calculators & Simulators")
option = st.sidebar.selectbox("Choose a calculator:", 
                             ["Loan Calculator", "Investment Growth", "Budget Tracker", "Retirement Calculator"])

# Render the appropriate calculator based on user selection
if option == "Loan Calculator":
    loan_calculator()
elif option == "Investment Growth":
    investment_calculator()
elif option == "Budget Tracker":
    budget_calculator()
elif option == "Retirement Calculator":
    retirement_calculator()
