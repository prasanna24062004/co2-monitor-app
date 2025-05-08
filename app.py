import streamlit as st
from simulator import simulate_co2
import streamlit.components.v1 as components

st.title("🫁 CO₂ Level Health Simulation")

# User Inputs
respiration_rate = st.slider("Respiration Rate (breaths/min)", 10, 40, 16)
heart_rate = st.slider("Heart Rate (bpm)", 50, 160, 75)
spo2 = st.slider("Oxygen Saturation (%)", 80, 100, 98)

# Simulate CO2 level
co2_level, status = simulate_co2(respiration_rate, heart_rate, spo2)

# Display Results
st.metric("Simulated CO₂ Level", f"{co2_level} ppm")
st.metric("Status", status)

# Trigger Alarm when CO2 level is Critical
if status == "Critical":
    st.error("⚠️ Critical CO₂ Level! Immediate action required!")
    
    # Play Alarm Sound (Autoplay)
    components.html("""
        <audio autoplay>
            <source src="https://raw.githubusercontent.com/prasanna24062004/co2-monitor-app/main/alarm.mp3" type="audio/mpeg">
        </audio>
    """, height=0)

elif status == "Warning":
    st.warning("🚨 Elevated CO₂ Level! Monitor closely.")
else:
    st.success("✅ CO₂ Level is Normal.")

