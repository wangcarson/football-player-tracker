# type: ignore
from ultralytics import YOLO

# Load model
model = YOLO("yolo11n.pt")
# model = YOLO("models/best.pt")

# Predict using model
results = model.predict('videos/08fd33_4.mp4', save=True)

# Print results
print(results[0])
if results[0].boxes:
    for box in results[0].boxes:
        print(box)