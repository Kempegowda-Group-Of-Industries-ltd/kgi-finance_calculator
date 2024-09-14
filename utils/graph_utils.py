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
