import cv2
from ultralytics import YOLO
model = YOLO("yolov8m.pt")
path = input("Image ya Video ka path do: ")
if path.endswith((".jpg", ".jpeg", ".png")):
    print("This is a image")
    # image code 
    image=cv2.imread(path)
    results =  model(image)
    annotated = results[0].plot()
    cv2.imshow("image_detection",annotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif path.endswith((".mp4", ".avi", ".mov")):
    print("This is a video")
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    while True:
        ret,frame=cap.read()
        if not ret:
            print("Could not read frame")
            break
        results = model(frame)
        annotated = results[0].plot()
        cv2.imshow("video_detection",annotated)
        if cv2.waitKey(int(1000/fps)) & 0XFF == ord('q'):
            break
    cap.release()
cv2.destroyAllWindows()

