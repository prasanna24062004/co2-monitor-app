import streamlit as st
from simulator import simulate_co2
from playsound import playsound
import threading

def play_alarm():
    playsound('alarm.mp3')

st.title("🫁 CO₂ Level Health Simulation")

respiration_rate = st.slider("Respiration Rate (breaths/min)", 10, 40, 16)
heart_rate = st.slider("Heart Rate (bpm)", 50, 160, 75)
spo2 = st.slider("Oxygen Saturation (%)", 80, 100, 98)

co2_level, status = simulate_co2(respiration_rate, heart_rate, spo2)

st.metric("Simulated CO₂ Level", f"{co2_level} ppm")
st.metric("Status", status)

# Trigger alarm sound for critical CO2 level
if status == "Critical":
    st.error("⚠️ Critical CO₂ Level! Immediate action required!")
    threading.Thread(target=play_alarm).start()
elif status == "Warning":
    st.warning("🚨 Elevated CO₂ Level! Monitor closely.")
else:
    st.success("✅ CO₂ Level is Normal.")
