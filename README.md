# 🚦 AI-Based Traffic Signal Optimization System

## 📌 Overview
This project is a computer vision-based traffic analysis system that detects and classifies vehicles from video feeds using YOLOv8. It estimates traffic density and adjusts signal timing using a rule-based optimization approach.

The goal is to reduce waiting time at intersections by dynamically responding to real-time traffic conditions instead of fixed-timer signals.

---

## ❗ Problem Statement
Traditional traffic signals operate on fixed timers, which do not adapt to real-time traffic conditions. This often leads to:
- Unnecessary waiting time
- Traffic congestion
- Inefficient road usage

---

## 💡 Proposed Solution
We built a prototype system that:
- Detects vehicles in real-time using YOLOv8
- Estimates traffic density based on detected vehicles
- Applies a heuristic scoring system to adjust signal timing dynamically

---

## ⚙️ Features
- Real-time vehicle detection using YOLOv8
- Vehicle classification (Car, Bus, Truck, Bike)
- Traffic density estimation
- Rule-based signal timing adjustment
- Starvation prevention logic (maximum wait threshold)
- Traffic analytics visualization
- Streamlit-based dashboard interface
- Supports both image and video input

---

## 🛠 Tech Stack
- Python
- YOLOv8 (Ultralytics)
- OpenCV
- NumPy
- Matplotlib
- Streamlit

---

## 🧠 Approach / Logic

### Vehicle Detection
YOLOv8 model is used to detect vehicles from each frame of video input.

### Traffic Scoring
Signal priority is calculated using:
- Vehicle count
- Vehicle type weights
- Waiting time

**Vehicle Weights:**

| Vehicle | Weight |
|---------|--------|
| Car     | 1.0    |
| Bike    | 0.5    |
| Bus     | 3.0    |
| Truck   | 3.0    |

### Signal Timing Formula
```
Priority Score = (vehicle_count × avg_weight × 1.5) + (wait_time × 2)
```

---

## 📂 Project Structure
```
Traffic_AI_Project/
│
├── detection.py      # YOLOv8-based vehicle detection
├── counting.py       # Vehicle counting logic
├── timer_logic.py    # Signal timing algorithm
├── dashboard.py      # Streamlit web dashboard
└── README.md
```

---

## 📸 Screenshots

### Dashboard
![Dashboard]
<img width="1366" height="728" alt="AI Traffic Controller and 21 more pages - Personal - Microsoft​ Edge 09-06-2026 02_09_12" src="https://github.com/user-attachments/assets/f6ab465a-5174-44d2-8470-b340d84fc5f2" />


### Vehicle Detection
![Detection]
<img width="1366" height="728" alt="AI Traffic Controller and 21 more pages - Personal - Microsoft​ Edge 09-06-2026 02_46_24" src="https://github.com/user-attachments/assets/e8484f24-add3-48cc-a775-fd958ed57f2c" />

<img width="1366" height="728" alt="AI Traffic Controller and 21 more pages - Personal - Microsoft​ Edge 09-06-2026 02_46_06" src="https://github.com/user-attachments/assets/901542cb-c280-4330-baa8-55617d7d0d47" />

<img width="1366" height="728" alt="Claude 09-06-2026 02_45_52" src="https://github.com/user-attachments/assets/0396a774-4c66-4c92-b830-af3c92812cd4" />

---

## ▶️ How to Run

**1. Install dependencies**
```bash
pip install ultralytics opencv-python streamlit matplotlib numpy
```

**2. Run dashboard**
```bash
streamlit run dashboard.py
```

---

## 📊 Output
- Live vehicle detection on video/image input
- Real-time traffic density estimation
- Dynamic signal timing visualization
- Graph-based traffic analytics

---

## 🚀 Future Improvements
- Multi-lane (4-direction) traffic management
- Emergency vehicle priority detection (ambulance/fire)
- DeepSORT-based vehicle tracking for accurate counting
- Reinforcement Learning-based signal optimization
- Real-world CCTV integration

---

## 👩‍💻 Developer
Built in 3 days as a hands-on learning project
combining Computer Vision and Web Development.

---

## 📌 Note
This is a prototype system demonstrating computer vision-based traffic analysis and rule-based optimization. It can be extended into a full reinforcement learning-based adaptive traffic control system.
