from ultralytics import YOLO
model = YOLO('.\models\yolov8n.pt').cuda()

results = model.train(
    data='.\data\signlang.yaml',
    epochs=100,
    device=0,
    pretrained=False,
    val=True,
    imgsz=640,
    batch=16,
    name='signlang_v1',
)
