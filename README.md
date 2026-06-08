# 🚦 AI Smart Traffic Signal Controller

## Project Overview
An AI-powered traffic signal controller that uses 
YOLOv8 to detect vehicles in real-time and 
dynamically adjusts signal timing based on 
traffic density.

## Problem Statement
Traditional traffic signals use fixed timers 
regardless of actual traffic — causing unnecessary 
jams and fuel waste.

## Solution
Our AI system analyzes live camera feed and 
automatically adjusts green light duration based 
on vehicle count, vehicle type, and wait time.

## Features
- Real-time vehicle detection (YOLOv8)
- Dynamic signal timer algorithm
- Vehicle type classification (Car, Bus, Truck, Bike)
- Priority scoring system
- Starvation prevention (force green after 45s)
- Live traffic analytics graph
- Web dashboard (Streamlit)
- Supports both image and video input

## Tech Stack
- Python
- YOLOv8 (Ultralytics)
- OpenCV
- Streamlit
- Matplotlib
- NumPy

## How to Run
pip install ultralytics streamlit opencv-python matplotlib numpy

streamlit run dashboard.py

## Project Structure
Traffic_AI_Project/
├── detection.py      
├── counting.py         
├── timer_logic.py     
├── dashboard.py       
└── README.md

## Algorithm
Priority Score = (vehicle_count × avg_weight × 1.5) 
                + (wait_time × 2)

Vehicle Weights:
- Car   = 1.0
- Bike  = 0.5
- Bus   = 3.0
- Truck = 3.0

## Built In
3 days as a first real-world AI project.

## Future Improvements
- 4-lane traffic management (North, South, East, West)
- Ambulance/Emergency vehicle priority detection
- Custom YOLOv8 training for Indian vehicles
- Real CCTV camera integration
