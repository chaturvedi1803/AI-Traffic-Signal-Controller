import cv2
from ultralytics import YOLO
#2. Model load karo
model = YOLO("yolov8m.pt")

#3. Video load karo (user input)
path = input("Enter the video path: ")
cap = cv2.VideoCapture(path)
fps = cap.get(cv2.CAP_PROP_FPS)

#4. max_count = 0 (loop ke bahar)
max_count = 0

#5. While loop
while True:

#6. Frame uthao
    ret,frame=cap.read()
    if not ret:
        print("Could not load frame")
        break

    frame = cv2.resize(frame, (640, 560))

    vehicle_count=0
    results = model(frame, conf=0.25)

    for box in results[0].boxes:
        cls_id=int(box.cls[0])
        if cls_id in [2,3,5,7]:
            vehicle_count+= 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame,(x1, y1),(x2, y2),(0,0,255),2)

    if vehicle_count > max_count:
        max_count =  vehicle_count

    cv2.putText(
    frame,                    # 1. image
    f"Count: {vehicle_count}",# 2. text jo dikhana hai
    (20, 50),                 # 3. position (x,y)--screen par hi hai uper
    cv2.FONT_HERSHEY_SIMPLEX, # 4. font style
    1.5,                      # 5. font size
    (0, 0, 255),              # 6. color (BGR) — red
    3                         # 7. thickness
    )

    cv2.imshow("video", frame)
    if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"Max vehicles at once: {max_count}")







