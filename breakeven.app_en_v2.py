import streamlit as st

def calculate_break_even(investment, implementation_cost, time_saved_per_project, hourly_rate, num_projects, license_revenue):
    total_cost = investment + implementation_cost
    annual_savings = time_saved_per_project * hourly_rate * num_projects
    net_annual_savings = annual_savings + license_revenue
    return total_cost / net_annual_savings if net_annual_savings > 0 else float('inf')

st.title("Break-even calculator PALAU")

investment = st.number_input("Investment (€)", min_value=0, value=100000)
implementation_cost = st.number_input("Implementation cost (€)", min_value=0, value=50000)
time_saved_per_project = st.number_input("Time saved per project", min_value=0, value=50)
hourly_rate = st.number_input("Hourly rate (€)", min_value=1, value=100)
num_projects = st.number_input("Number of projects per year", min_value=1, value=20)

# Neue Variablen für Lizenzeinnahmen
num_licenses = st.number_input("Number of free licences", min_value=0, value=5)
license_price = st.number_input("Licence price (€)", min_value=0, value=1000)
license_revenue = num_licenses * license_price

if st.button("Calculate"):
    break_even_years = calculate_break_even(investment, implementation_cost, time_saved_per_project, hourly_rate, num_projects, license_revenue)
    st.write(f"Break-even in **{break_even_years:.2f} years**")
