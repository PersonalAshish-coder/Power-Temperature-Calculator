import streamlit as st

st.title("🔥 Power–Temperature Calculator (Water)")

st.write("Uses formula: P × t = m × c × ΔT")

# Inputs
power = st.text_input("Enter Power (Watts)")
mass = st.text_input("Enter Mass (kg)")
T = st.text_input("Enter Temperature Change (°C)")
time = st.text_input("Enter Time (minutes)")

c = 4186  # constant for water

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