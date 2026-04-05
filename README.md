# 🛡️ IoT Healthcare Honeypot System

## 📌 Project Overview

This project is an **IoT-based Healthcare Honeypot System** designed to simulate vulnerable healthcare devices and capture malicious activities from attackers.
The goal is to analyze real-world cyberattacks and improve security awareness in IoT healthcare environments.

---

## 🎯 Objectives

* Simulate IoT healthcare devices (e.g., patient monitors, sensors)
* Attract attackers using a controlled honeypot environment
* Capture and log attacker activities
* Analyze attack patterns such as IP addresses and commands used

---

## 🛠️ Technologies Used

* **Kali Linux**
* **Python 3**
* Networking tools and libraries
* Log analysis scripts

---

## ⚙️ Project Structure

```
iot-honeypot-healthcare/
│
├── logs/                # Stores attacker logs
├── parser/              # Log parsing scripts
├── scripts/             # Honeypot setup scripts
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/your-username/honeypot-healthcare.git
cd honeypot-healthcare
```

---

### 2. Install Dependencies

```
pip3 install -r requirements.txt
```

---

### 3. Run the Honeypot

```
python3 main.py
```

---

### 4. Analyze Logs

```
cd parser
python3 parse_logs.py
```

---

## 📊 Output

The system captures and displays:

* Top attacker IP addresses
* Commands executed by attackers
* Activity logs for further analysis

---

## 🔐 Key Features

* Real-time attack logging
* Lightweight and easy to deploy
* Simulated healthcare IoT environment
* Log analysis for cybersecurity insights

---

## 🧪 Use Case

This project can be used for:

* Cybersecurity learning and research
* Understanding attacker behavior
* Demonstrating IoT vulnerabilities
* Academic and internship projects

---

## ⚠️ Disclaimer

This project is created for **educational purposes only**.
Do not deploy this system on production networks without proper authorization.

---

## 👩‍💻 Author

**Sharvari Deshbhratar**

---

## ⭐ Future Improvements

* Dashboard for real-time monitoring
* Integration with SIEM tools
* Advanced attack detection using AI/ML
* Improved visualization of logs

---
##UPDATE 
- Added honeypot environment setup
- Improved logging mechanism 
