import streamlit as st
import pandas as pd

def budget_calculator():
    st.header("Budget Tracker")
    
    # Input fields for income and expenses
    income = st.number_input("Monthly Income", min_value=0.0, step=100.0)
    expense_categories = st.text_area("Expense Categories (separate by commas)", "Rent, Groceries, Utilities, Transport")
    expenses = {}
    
    for category in expense_categories.split(","):
        category = category.strip()
        expenses[category] = st.number_input(f"{category} Expense", min_value=0.0, step=50.0)
    
    # Total expenses and savings
    total_expenses = sum(expenses.values())
    savings = income - total_expenses
    
    # Show breakdown
    st.write(f"**Total Expenses:** ₹{total_expenses:,.2f}")
    st.write(f"**Savings:** ₹{savings:,.2f}")

    # Pie chart visualization
    if total_expenses > 0:
        st.write("**Expense Breakdown**")
        expense_data = pd.DataFrame.from_dict(expenses, orient="index", columns=["Amount"])
        st.bar_chart(expense_data)
