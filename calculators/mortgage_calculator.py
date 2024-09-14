import numpy_financial as npf

def mortgage_calculator():
    loan_amount = st.number_input("Loan Amount", min_value=0.0, value=1000000.0)
    annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=5.0)
    years = st.number_input("Loan Term (Years)", min_value=0, value=30)

    total_months = years * 12
    monthly_rate = (annual_rate / 100) / 12

    # Calculate monthly payment using numpy_financial
    monthly_payment = npf.pmt(monthly_rate, total_months, -loan_amount)

    st.write(f"**Monthly Payment:** ₹{monthly_payment:,.2f}")

    months = np.arange(1, total_months + 1)

    remaining_balance = []
    for month in months:
        balance = npf.fv(monthly_rate, month, -monthly_payment, loan_amount)
        remaining_balance.append(balance)

    data = {
        "Month": months,
        "Remaining Balance": remaining_balance
    }

    df = pd.DataFrame(data)
    st.write(df)
    plot_amortization_schedule(df)
