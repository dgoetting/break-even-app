import streamlit as st

def calculate_break_even(investment, template_cost, time_saved_per_project, hourly_rate, num_projects):
    total_cost = investment + template_cost
    annual_savings = time_saved_per_project * hourly_rate * num_projects
    return total_cost / annual_savings if annual_savings > 0 else float('inf')

st.title("Break-even-Rechner für Nachhaltigkeitssoftware")

investment = st.number_input("Investitionssumme (€)", min_value=0, value=100000)
template_cost = st.number_input("Kosten für Template-Erstellung (€)", min_value=0, value=50000)
time_saved_per_project = st.number_input("Eingesparte Stunden pro Projekt", min_value=0, value=50)
hourly_rate = st.number_input("Stundensatz (€)", min_value=1, value=100)
num_projects = st.number_input("Anzahl der Projekte pro Jahr", min_value=1, value=20)

if st.button("Berechnen"):
    break_even_years = calculate_break_even(investment, template_cost, time_saved_per_project, hourly_rate, num_projects)
    st.write(f"Break-even in **{break_even_years:.2f} Jahren**")
