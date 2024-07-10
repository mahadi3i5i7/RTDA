if __name__ == '__main__':

    from ultralytics import YOLO

    # pre-trained model weights for transfer learning
    model = YOLO('yolov8m.pt')

    # training on GPU
    results = model.train(
        data= 'path to data.yaml',
        imgsz=640,
        epochs=100,
        patience=30,
        device="0",
        batch=12,
        name='YOLOv8M_640_12_100_epochs'
    )



