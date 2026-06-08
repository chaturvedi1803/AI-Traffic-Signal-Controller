import streamlit as st
import cv2
import tempfile
import numpy as np
from ultralytics import YOLO
import time
import matplotlib.pyplot as plt
from timer_logic import calculate_score, get_green_time, get_signal_color

st.set_page_config(
    page_title="AI Traffic Controller",
    page_icon="🚦",
    layout="wide"
)

# Style mein ye add karo:
st.markdown("""
<style>
.stApp {
    background-color: #0f0f1a;
    color: Coral;
}
.stMetric {
    background-color: #1a1a2e;
    padding: 10px;
    border-radius: 10px;
}
/* Upload button fix */
.stFileUploader {
    background-color: #1a1a2e !important;
    border: 2px solid #00ff88 !important;
    border-radius: 10px !important;
}
.stFileUploader label {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("# 🚦 AI Smart Traffic Signal Controller")
st.markdown("### Real-time Vehicle Detection & Dynamic Signal Management")
st.markdown("---")

model = YOLO("yolov8n.pt")

uploaded_file = st.file_uploader(
    "📤 Traffic Video ya Image Upload Karo",
    type=["mp4", "avi", "mov", "jpg", "jpeg", "png"]
)

# uploaded_file check se PEHLE add karo:
if uploaded_file is None:
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    col1.success("### 🚗 Vehicle Detection\n""Real-time vehicle detection powered by YOLOv8 AI")
    col2.warning("### 🚦 Dynamic Signal Control\n""Signal timing is adjusted based on traffic density")
    col3.info("### 📊 Live Analytics\n""Real-time traffic graphs and vehicle breakdown")
    st.markdown("---")
    st.markdown("### 🎯 Getting Started")
    st.markdown("""
    1. Upload a **traffic image or video**
    2. The system will **analyze the traffic scene**
    3. Vehicles will be **detected and classified automatically**
    4. Traffic density, signal timing, and analytics will be displayed in real time
    """)

if uploaded_file is not None:
    file_type = uploaded_file.type

    if "image" in file_type:
        file_bytes = np.asarray(
            bytearray(uploaded_file.read()),
            dtype=np.uint8
        )
        frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        results = model(frame, conf=0.35)[0]

        vehicles = []
        for box in results.boxes:
            cls_id = int(box.cls[0])
            if cls_id in [2, 3, 5, 7]:
                vehicles.append(cls_id)
                x1,y1,x2,y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

        score = calculate_score(vehicles, wait_time=0)
        green_time = get_green_time(score)
        signal = get_signal_color(score)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📸 Detection Result")
            st.image(frame, channels="BGR", width=600)  # ✅ Fixed

        with col2:
            st.subheader("🚦 Signal Status")
            m1, m2 = st.columns(2)
            m1.metric("🚗 Vehicles", len(vehicles))
            m2.metric("📊 Score", round(score, 2))
            st.markdown("---")

            if "CRITICAL" in signal:
                st.error(f"🚨 {signal}")
            elif "GREEN" in signal:
                st.success(f"🟢 {signal}")
            elif "YELLOW" in signal:
                st.warning(f"🟡 {signal}")
            else:
                st.error(f"🔴 {signal}")

            st.info(f"⏱️ Green Time: {green_time} seconds")
            st.markdown("---")
            st.subheader("📋 Vehicle Breakdown")

            c1,c2,c3,c4 = st.columns(4)
            c1.metric("🚗 Cars",   vehicles.count(2))
            c2.metric("🏍️ Bikes",  vehicles.count(3))
            c3.metric("🚌 Buses",  vehicles.count(5))
            c4.metric("🚛 Trucks", vehicles.count(7))

    elif "video" in file_type:
        tfile = tempfile.NamedTemporaryFile(
            delete=False, suffix=".mp4"
        )
        tfile.write(uploaded_file.read())

        cap = cv2.VideoCapture(tfile.name)
        fps = cap.get(cv2.CAP_PROP_FPS)
        red_start = time.time()
        count_history = []

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📹 Live Feed")
            video_placeholder = st.empty()

        with col2:
            st.subheader("🚦 Signal Status")
            signal_placeholder = st.empty()
            timer_placeholder  = st.empty()
            st.markdown("---")
            m1, m2 = st.columns(2)
            count_placeholder = m1.empty()
            score_placeholder = m2.empty()
            st.markdown("---")
            st.subheader("📋 Live Breakdown")
            b1,b2,b3,b4 = st.columns(4)
            cars_ph   = b1.empty()
            bikes_ph  = b2.empty()
            buses_ph  = b3.empty()
            trucks_ph = b4.empty()

        st.markdown("---")
        st.subheader("📊 Live Traffic Graph")
        graph_placeholder = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame, conf=0.35)[0]
            vehicles = []

            for box in results.boxes:
                cls_id = int(box.cls[0])
                if cls_id in [2, 3, 5, 7]:
                    vehicles.append(cls_id)
                    x1,y1,x2,y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

            wait_time  = time.time() - red_start
            score      = calculate_score(vehicles, wait_time)
            green_time = get_green_time(score)
            signal     = get_signal_color(score)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            video_placeholder.image(frame_rgb, width=600)  # ✅ Fixed

            if "CRITICAL" in signal:
                signal_placeholder.error(f"🚨 {signal}")
            elif "GREEN" in signal:
                signal_placeholder.success(f"🟢 {signal}")
            elif "YELLOW" in signal:
                signal_placeholder.warning(f"🟡 {signal}")
            else:
                signal_placeholder.error(f"🔴 {signal}")

            timer_placeholder.info(
                f"⏱️ Green Time: {green_time}s | "
                f"Wait: {int(wait_time)}s"
            )

            count_placeholder.metric("🚗 Vehicles", len(vehicles))
            score_placeholder.metric("📊 Score", round(score,2))

            cars_ph.metric("🚗",   vehicles.count(2))
            bikes_ph.metric("🏍️",  vehicles.count(3))
            buses_ph.metric("🚌",  vehicles.count(5))
            trucks_ph.metric("🚛", vehicles.count(7))

            count_history.append(len(vehicles))
            if len(count_history) % 5 == 0:
                fig, ax = plt.subplots(figsize=(8,3))
                ax.plot(count_history, color='#00ff88', linewidth=2)
                ax.fill_between(
                    range(len(count_history)),
                    count_history,
                    alpha=0.3,
                    color='#00ff88'
                )
                ax.set_facecolor('#1a1a2e')
                fig.patch.set_facecolor('#1a1a2e')
                ax.tick_params(colors='white')
                ax.set_title("Live Vehicle Count", color='white')
                ax.set_xlabel("Frames", color='white')
                ax.set_ylabel("Count", color='white')
                graph_placeholder.pyplot(fig)
                plt.close()

        cap.release()
