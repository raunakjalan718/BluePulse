# BluePulse
Underground Water Leakge Detection System
# Noobventures
# Raunak Jalan
# Shrivatsa S Kulkarni
# Bhavashesh Dachpalli

# You can check the implementation of our IOT at [https://youtu.be/9BgTsOEIfLc](https://youtu.be/fAw9PgAj71Y)

#### **Problem Statement 2: Water Conservation and Management**  
#### **Overview:**  
Water scarcity is a growing concern worldwide. Efficient water management systems can significantly reduce water wastage and ensure sustainable usage. The objective is to create a **smart IoT-based system** for monitoring and controlling water usage in buildings using **real-time data, predictive analytics, and automation**.  

#### **Tech Stack:**  
- **IoT Components:** ESP32, YF-S201 Hall Effect Water Flow Sensor, Water Pressure Sensor, Leakage Detection Sensor, LCD with I2C, 10K Potentiometer.  
- **Machine Learning & Data Processing:** Python (Pandas, NumPy, Joblib, Scikit-learn, Matplotlib, Seaborn).  
- **Database:** MySQL for storing sensor data and water usage history.  
- **Web Application:** React.js for an interactive dashboard displaying real-time analytics.  
- **Cloud Infrastructure:** AWS/GCP/Azure for data storage and real-time processing.  

#### **Task:**  
Develop a **smart water management system** that includes:  
✔ **IoT sensors** to monitor water flow, detect leaks, and measure usage in real-time.  
✔ **Machine Learning-powered predictive analytics** to forecast water demand and identify wastage patterns.  
✔ **A React-based web application** to display water usage statistics, alerts, and conservation tips.  
✔ **Integration with existing building management systems** for automated water control and alerts.  

#### **Resources:**  
- **IoT Hardware:** ESP32, Water Flow & Pressure Sensors, LCD Display.  
- **Machine Learning Frameworks:** Pandas, NumPy, Scikit-learn for analysis.  
- **Database Management:** MySQL for structured data storage.  
- **Frontend Development:** React.js for the user dashboard.  
- **Cloud Storage & Processing:** AWS/GCP/Azure for handling real-time data.  

USE bluepulse;
SHOW TABLES;
SELECT * FROM pipeline1 LIMIT 10;
python new_modell.py
uvicorn iot_fast_api:app --host 0.0.0.0 --port 8000 --reload
uvicorn main:app --reload
curl -X POST "http://localhost:8000/add-pipeline-data" -H "Content-Type: application/json" -d '{"timestamp": "2025-02-09T11:00:00", "flow_inlet": 100, "flow_outlet": 90}'
npm install"
npm start
