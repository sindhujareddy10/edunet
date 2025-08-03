import streamlit as st
import numpy as np
import joblib  

# Load the trained model
model = joblib.load("Farm_Irrigation_System.pkl")  

st.title("💧 Smart Sprinkler System 🌿")
st.subheader("Enter scaled sensor values (0 to 1) to predict sprinkler status")

# Collect sensor inputs (scaled values)
sensor_values = []
for i in range(20):
    val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    sensor_values.append(val)

# Predict button
if st.button("🔍 Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("### 🌡️ Prediction Results:")
    for i, status in enumerate(prediction):
        if status == 1:
            st.markdown(f"<span style='color:blue'>Sprinkler {i} (parcel_{i}): 🔵 ON</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<span style='color:red'>Sprinkler {i} (parcel_{i}): 🔴 OFF</span>", unsafe_allow_html=True)
