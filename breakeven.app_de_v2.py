import streamlit as st

def calculate_break_even(investment, template_cost, time_saved_per_project, hourly_rate, num_projects, license_revenue):
    total_cost = investment + template_cost
    annual_savings = time_saved_per_project * hourly_rate * num_projects
    net_annual_savings = annual_savings + license_revenue
    return total_cost / net_annual_savings if net_annual_savings > 0 else float('inf')

st.title("Break-even-Rechner für Nachhaltigkeitssoftware")

investment = st.number_input("Investitionssumme (€)", min_value=0, value=100000)
template_cost = st.number_input("Kosten für Template-Erstellung (€)", min_value=0, value=50000)
time_saved_per_project = st.number_input("Eingesparte Stunden pro Projekt", min_value=0, value=50)
hourly_rate = st.number_input("Stundensatz (€)", min_value=1, value=100)
num_projects = st.number_input("Anzahl der Projekte pro Jahr", min_value=1, value=20)

# Neue Variablen für Lizenzeinnahmen
num_licenses = st.number_input("Anzahl der kostenlosen Lizenzen", min_value=0, value=5)
license_price = st.number_input("Lizenzpreis pro Kunde (€)", min_value=0, value=1000)
license_revenue = num_licenses * license_price

if st.button("Berechnen"):
    break_even_years = calculate_break_even(investment, template_cost, time_saved_per_project, hourly_rate, num_projects, license_revenue)
    st.write(f"Break-even in **{break_even_years:.2f} Jahren**")
