import streamlit as st

def calculate_break_even(investment, template_cost, time_saved_per_project, hourly_rate, num_projects):
    total_cost = investment + template_cost
    annual_savings = time_saved_per_project * hourly_rate * num_projects
    return total_cost / annual_savings if annual_savings > 0 else float('inf')

st.title("Break-even-calculator PALAU")

investment = st.number_input("Investment (€)", min_value=0, value=100000)
template_cost = st.number_input("Costs template creation (€)", min_value=0, value=50000)
time_saved_per_project = st.number_input("Saved hours per project", min_value=0, value=50)
hourly_rate = st.number_input("Hourly rate (€)", min_value=1, value=100)
num_projects = st.number_input("Number of projects per year", min_value=1, value=20)

if st.button("Calculate"):
    break_even_years = calculate_break_even(investment, template_cost, time_saved_per_project, hourly_rate, num_projects)
    st.write(f"Break-even in **{break_even_years:.2f} years**")
