def simulate_co2(respiration_rate, heart_rate, spo2):
    if respiration_rate > 25 or spo2 < 90:
        return 1000, "Critical"
    elif respiration_rate > 18 or spo2 < 95:
        return 700, "Warning"
    else:
        return 400, "Normal"
