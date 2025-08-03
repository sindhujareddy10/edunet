🌱 Smart Irrigation System 💧
A Smart Irrigation System built using Machine Learning and Streamlit to predict the status of irrigation (ON/OFF) based on real-time environmental sensor data. This project helps farmers or gardeners optimize water usage effectively.

🚀 Features
📊 Real-time prediction using trained ML model (Farm_Irrigation_System.pkl)

🌡️ Inputs: Temperature, Humidity, Soil Moisture, Soil Type, Crop Type

📁 Uses sensor data from irrigation_machine.csv

🌐 User-friendly web app interface built with Streamlit

🔘 "Predict" button with customized color

🟢🛑 Emoji display for irrigation status (🟢 ON / 🔴 OFF)

🔁 Predicts for 20 random samples from the dataset

🧠 Model
RandomForestClassifier wrapped in MultiOutputClassifier

Trained on labeled environmental data

Saved as Farm_Irrigation_System.pkl using joblib

📁 Project Structure

smart_irrigation/
├── irrigation_machine.csv           # Input sensor data
├── Farm_Irrigation_System.pkl       # Trained model
├── app.py                           # Main Streamlit application
├── requirements.txt                 # Required Python packages
└── README.md                        # Project documentation
▶️ How to Run
Clone the repository:


git clone https://github.com/sindhuajreddy10/edunet
cd smart_irrigation
Install dependencies:


pip install -r requirements.txt

Run the app:


streamlit run app.py
🧪 Sample Output
Input features: temperature = 27°C, humidity = 60%, moisture = 30%, soil = loamy, crop = rice

Prediction:

Irrigation: 🔴 OFF

📦 Requirements
Python 3.8+

pandas

scikit-learn

joblib

streamlit

📌 Future Improvements
Integrate real-time sensor hardware via IoT

Add user login for multiple farms

Historical data analytics & dashboard

Mobile-friendly UI
