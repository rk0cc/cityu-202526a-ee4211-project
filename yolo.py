#Load YOLO from Ultralytics library
from ultralytics import YOLO

#Load YOLO Object Detection Model
model = YOLO("yolo11n.pt")

#Sample tracking w/ Camera
results = model.track(source=0, show=True)