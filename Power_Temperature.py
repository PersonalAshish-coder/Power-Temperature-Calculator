import streamlit as st

st.title("🔥 Power–Temperature Calculator")

st.write("Uses formula: P × t = m × c × ΔT")

# Substance selection
substance = st.selectbox(
    "Select Substance",
    [
        "Water",
        "Milk",
        "Vegetable Oil",
        "Sunflower Oil",
        "Mustard Oil",
        "Peanut Oil",
        "Olive Oil",
        "Corn Oil"
    ]
)

# Specific heat values (J/kg°C)
c_values = {
    "Water": 4186,
    "Milk": 3900,
    "Vegetable Oil": 3230,
    "Sunflower Oil": 3190,
    "Mustard Oil": 1670,
    "Peanut Oil": 2050,
    "Olive Oil": 1850,
    "Corn Oil": 1670
}

# Default c from selection
default_c = c_values[substance]

# Manual override option
use_custom_c = st.checkbox("✏️ Enter specific heat manually")

if use_custom_c:
    c = st.number_input("Enter specific heat capacity (J/kg°C)", min_value=0.0)
else:
    c = default_c
    st.info(f"Using c = {c} J/kg°C for {substance}")

# Optional warning for oils
if "Oil" in substance:
    st.warning("⚠️ Oil specific heat varies depending on type and temperature")

# Inputs
power = st.text_input("Enter Power (Watts)")
mass = st.text_input("Enter Mass (kg)")
T = st.text_input("Enter Temperature Change (°C)")
time = st.text_input("Enter Time (minutes)")

# Convert inputs
def convert(val):
    return float(val) if val.strip() != "" else None

power = convert(power)
mass = convert(mass)
T = convert(T)
time = convert(time)

if time is not None:
    time = time * 60  # minutes → seconds

# Button
if st.button("Calculate"):

    values = [power, mass, T, time]
    
    if values.count(None) != 1:
        st.error("❌ Please leave exactly ONE field empty")
    
    elif c == 0:
        st.error("❌ Specific heat (c) cannot be zero")
    
    else:
        try:
            if power is None:
                result = mass * c * T / time
                st.success(f"Power = {result:.2f} W")

            elif time is None:
                result = (mass * c * T / power) / 60
                st.success(f"Time = {result:.2f} minutes")

            elif mass is None:
                result = power * time / (c * T)
                st.success(f"Mass = {result:.2f} kg")

            elif T is None:
                result = power * time / (mass * c)
                st.success(f"Temperature Change = {result:.2f} °C")

        except ZeroDivisionError:
            st.error("❌ Division by zero error (check inputs)")