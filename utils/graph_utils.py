import matplotlib.pyplot as plt
import streamlit as st

def plot_amortization_schedule(data):
    fig, ax = plt.subplots()
    ax.plot(data["Remaining Balance"], label="Remaining Balance")
    ax.plot(data["Principal Paid"], label="Principal Paid")
    ax.plot(data["Interest Paid"], label="Interest Paid")
    ax.legend()
    st.pyplot(fig)

def plot_investment_growth(months, growth):
    fig, ax = plt.subplots()
    ax.plot(months, growth, label="Investment Growth")
    ax.set_xlabel("Months")
    ax.set_ylabel("Value (₹)")
    st.pyplot(fig)

def plot_retirement_projection(months, growth):
    fig, ax = plt.subplots()
    ax.plot(months, growth, label="Retirement Savings")
    ax.set_xlabel("Months")
    ax.set_ylabel("Value (₹)")
    st.pyplot(fig)

import matplotlib.pyplot as plt
import streamlit as st

def plot_amortization_schedule(data):
    """Plots the amortization schedule with remaining balance, principal paid, and interest paid."""
    fig, ax = plt.subplots()
    
    ax.plot(data["Remaining Balance"], label="Remaining Balance", color='blue', linestyle='-', linewidth=2)
    ax.plot(data["Principal Paid"], label="Principal Paid", color='green', linestyle='--', linewidth=2)
    ax.plot(data["Interest Paid"], label="Interest Paid", color='red', linestyle='-.', linewidth=2)
    
    ax.set_xlabel("Months")
    ax.set_ylabel("Amount (₹)")
    ax.set_title("Amortization Schedule")
    ax.legend()
    ax.grid(True)
    
    st.pyplot(fig)

def plot_investment_growth(months, growth):
    """Plots the investment growth over time."""
    fig, ax = plt.subplots()
    
    ax.plot(months, growth, label="Investment Growth", color='purple', linestyle='-', linewidth=2)
    
    ax.set_xlabel("Months")
    ax.set_ylabel("Value (₹)")
    ax.set_title("Investment Growth Over Time")
    ax.legend()
    ax.grid(True)
    
    st.pyplot(fig)

def plot_retirement_projection(months, growth):
    """Plots the retirement savings projection over time."""
    fig, ax = plt.subplots()
    
    ax.plot(months, growth, label="Retirement Savings", color='orange', linestyle='-', linewidth=2)
    
    ax.set_xlabel("Months")
    ax.set_ylabel("Value (₹)")
    ax.set_title("Retirement Savings Projection")
    ax.legend()
    ax.grid(True)
    
    st.pyplot(fig)

