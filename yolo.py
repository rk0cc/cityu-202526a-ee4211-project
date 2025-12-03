#Load YOLO from Ultralytics library
from ultralytics import YOLO

#Load YOLO Object Detection Model
model =YOLO("yolo11n-cls.yaml")
model = YOLO("yolo11n-cls.pt")
model = YOLO("yolo11n-cls.yaml").load("yolo11n-cls.pt") 

# Train the model
if __name__ == '__main__':
    results = model.train(data="datasets/cars_tanks/images", epochs=100, imgsz=256, device=0)