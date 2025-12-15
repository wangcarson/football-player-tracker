from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

results = model.predict('videos/08fd33_4.mp4', save=True)
print(results[0])

for box in results[0].boxes:
    print(box)