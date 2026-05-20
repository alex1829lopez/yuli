import streamlit as st

st.set_page_config(page_title="Conversor de Temperatura")

st.title("🌡️ Conversor de Temperatura")

# Entrada de datos
temperatura = st.number_input(
    "Ingresa la temperatura",
    value=0.0
)

unidad = st.selectbox(
    "Selecciona la unidad",
    ["Celsius", "Fahrenheit", "Kelvin"]
)

# Conversión
if unidad == "Celsius":
    fahrenheit = (temperatura * 9/5) + 32
    kelvin = temperatura + 273.15

    st.success(f"Fahrenheit: {fahrenheit:.2f} °F")
    st.success(f"Kelvin: {kelvin:.2f} K")

elif unidad == "Fahrenheit":
    celsius = (temperatura - 32) * 5/9
    kelvin = celsius + 273.15

    st.success(f"Celsius: {celsius:.2f} °C")
    st.success(f"Kelvin: {kelvin:.2f} K")

elif unidad == "Kelvin":
    celsius = temperatura - 273.15
    fahrenheit = (celsius * 9/5) + 32

    st.success(f"Celsius: {celsius:.2f} °C")
    st.success(f"Fahrenheit: {fahrenheit:.2f} °F")