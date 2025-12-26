from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction
from ultralytics import YOLO

def infer(config): 

    # Load YOLOv10x model from scratch
    model = YOLO("yolov10x.yaml")

    detection_model = AutoDetectionModel.from_pretrained(
        model_type='yolov8',
        model_path=model,
        confidence_threshold=0.2,
        device="cuda:0"
    )

    result = get_sliced_prediction(
        "/data/image.JPG",
        detection_model,
        slice_height = config['crop']['height'],
        slice_width = config['crop']['width'],
        overlap_height_ratio = 0.1,
        overlap_width_ratio = 0.1
    )