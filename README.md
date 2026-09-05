<div align="center">

# 🌊 EcoSentry: HAZARDMESH — AI-Powered Environmental Intelligence & Early Warning Network
### Smart India Hackathon (SIH 2026) | Problem ID: SIH26178 | Disaster Management Track

[![SIH Status](https://img.shields.io/badge/SIH-ID%20SIH26178-emerald?style=for-the-badge&logo=codeforces&logoColor=white)]()
[![Team](https://img.shields.io/badge/Team-EcoSentry%20(BMS%2FSIH2026%2F48)-blue?style=for-the-badge&logo=python&logoColor=white)]()
[![Hardware](https://img.shields.io/badge/Hardware-ESP32%20%7C%20LoRa%20%7C%20Edge%20AI-orange?style=for-the-badge&logo=arduino&logoColor=white)]()
[![Institution](https://img.shields.io/badge/BMSCE-BMS%20College%20of%20Engineering-purple?style=for-the-badge)]()

</div>

---

## 📌 Problem Statement Details
* **Problem Statement ID:** SIH26178
* **Problem Statement Title:** Flood Detection System (Environmental Intelligence Network)
* **Theme:** Disaster Management
* **PS Category:** Hardware
* **Team ID:** BMS/SIH2026/48
* **Team Name:** EcoSentry

---

### 📖 Background & Context
India faces a growing range of environmental and climate-related risks including urban flooding, river floods, cyclones, forest fires, air pollution, droughts, landslides, and extreme weather events. Floods remain among the most frequent disasters across states such as Assam, Bihar, Kerala, and Maharashtra. Traditional monitoring systems often depend on centralized infrastructure and fail to provide sufficiently localized, real-time intelligence during severe weather when communication towers collapse.

---

### 💡 Proposed Solution: HAZARDMESH
**HAZARDMESH** is a solar-powered, distributed network of sensor nodes deployed across rivers and forests that combines multi-hazard sensing, Edge AI, and LoRa communication to detect anomalies locally. 

Key innovations of our proposed solution include:
* **Edge-First Operation:** Processes sensor data locally to detect anomalies at the source, cutting latency and operating resiliently even during network and internet outages.
* **Hazard Propagation Intelligence:** Rather than just detecting that a hazard is happening at a specific spot, the system predicts where it is likely to spread next using upstream trends and neighboring node data.
* **Sensor TrustScore:** Continuously evaluates sensor health, consistency, and neighbor-node agreement to filter out false positives and sensor noise.
* **Compact Intelligence Packets:** Transmits lightweight, prioritized summary alerts over sub-GHz LoRa rather than bandwidth-heavy raw sensor streams.

---

## 🛠️ Technologies Used
* **Edge Computing & AI:** On-device anomaly detection algorithms running directly on microcontrollers for real-time risk assessment without cloud dependency.
* **Wireless Communication:** LoRa (Long Range) sub-GHz transceivers for peer-to-peer node communication and long-distance gateway data routing.
* **Microcontrollers & Vision:** ESP32 development boards and ESP32-CAM modules for local telemetry and surveillance.
* **Backend & Dashboard:** Python Flask server integrating live GIS mapping, sensor telemetry tables, and emergency alert monitoring.

---

## 📦 Components Used & Bill of Materials (BoM)
Our prototype is cost-effective, modular, and built using readily available hardware components:

| Component | Function / Description | Cost (₹) |
| :--- | :--- | :--- |
| **ESP32 Microcontroller** | Core processing unit and Wi-Fi/Bluetooth module | ₹400 |
| **Ultrasonic Sensor (JSN)** | Waterproof water level and distance measurement | ₹350 |
| **Li-Po Battery** | Rechargeable power source for field deployment | ₹180 |
| **Temperature Sensor (DS18B20)** | Precise environmental and water temperature tracking | ₹80 |
| **Rain Gauge** | Precipitation and rainfall rate measurement | ₹150 |
| **MPU 6050** | Seismic vibration and tilt detection | ₹150 |
| **5V Boost Converter** | Power regulation for sensors and peripherals | ₹130 |
| **Total Estimated Cost** | **Affordable, scalable hardware deployment** | **₹1,440** |

---

## ⚙️ System Architecture Workflow
[Sensor Inputs: Ultrasonic, Rain, Temperature, MPU6050, ESP32-CAM]
                                        │
                                        ▼
                        [Power-Saving Mode / Data Collection]
                                        │
                                        ▼
                        [ESP32 Onboard Edge AI Analysis]
                        (Local Anomaly & State Detection)
                                        │
                                        ▼
                             (Is State Normal?)
                             /                \
                       [ YES ]                [ NO ]
                         │                      │
                         ▼                      ▼
               [Route to SD Card Log]    [Disaster Threshold Exceeded?]
                 (Local Storage Audit)          │
                                       (If Yes / Emergency)
                                                │
                                                ▼
                                   [Packet Compression]
                                   (Metadata, GPS & Telemetry)
                                                │
                                                ▼
                                   [Onboard LoRa Transceiver]
                                   (Long-Range Sub-GHz Signal)
                                                │
                                                ▼
                                    [Central LoRa Gateway]
                                    (Ingests Sub-GHz Signals)
                                                │
                                                ▼
                                 [Python Flask Server & Dashboard]
                                 (GIS Mapping & Emergency Alerts)

🔍Quick Breakdown of the Flow Logic
**Normal State Branch (YES):** 
When the sensor readings are within safe baseline parameters, the ESP32 logs the telemetry locally to an onboard SD card for record-keeping without wasting transmission bandwidth.  
**Anomalous State Branch (NO):** 
If local Edge AI detects a threshold breach (such as rising water levels or seismic vibration), the node packages the incident, compresses the GPS and metadata, and immediately transmits a long-range packet via LoRa to bypass failed network infrastructure. 
                                 
## ⚡ Repository Structure
SIH-Flood-Monitoring-System/
├── public/
│   └── index.html       # Minimalist dark-mode real-time dashboard UI
├── src/
│   └── main.cpp         # ESP32 C++ firmware for sensor nodes & gateway
├── server.py            # Python Flask backend & serial communication handler
└── README.md            # Comprehensive project documentation

---
## 👥 Team Members
* **Team EcoSentry** (Team ID: `BMS/SIH2026/48`)
  
* **Pramod H Bhat** — BMS College of Engineering (BMSCE), Bangalore (ECE)
* **Proksh D K** — BMS College of Engineering (BMSCE), Bangalore (ECE)
* **Priyal S Kokanay** — BMS College of Engineering (BMSCE), Bangalore (ECE)
* **Muhammed Abshar K K** — BMS College of Engineering (BMSCE), Bangalore (ECE)
* **Pranav Vadgal** — BMS College of Engineering (BMSCE), Bangalore (ECE)
* **Moulya P** — BMS College of Engineering (BMSCE), Bangalore (ECE)
