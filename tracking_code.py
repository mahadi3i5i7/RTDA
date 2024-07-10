from collections import defaultdict
import cv2
import numpy as np
from ultralytics import YOLO
import time
import math
import pygame

import arduino_module
import serial

model = YOLO("best_model_weights.pt")
print(model.names)

arduino_module.check_port()

#video frames captured from camera
cap = cv2.VideoCapture(0)

# store the tracking history
track_history = defaultdict(lambda: {"track": [], "area": []})

def object_closeness_general(areafirst, arealast):
    closer_factor = 0
    if areafirst > 0:
        closer_factor = math.sqrt(arealast) / math.sqrt(areafirst)
    return round(closer_factor, 2)


# loop through frames
while cap.isOpened():
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True, tracker="BYTETRACK.yaml", imgsz=896, conf=0.6, device="0")


        for result in results:
            if result.boxes is None or result.boxes.id is None:
                resized_frame = cv2.resize(frame, (1536, 864))
                cv2.imshow("YOLOv8 Tracking", resized_frame)
                continue

            else:
                # Get the boxes and track IDs
                boxes = results[0].boxes.xywh
                track_ids = results[0].boxes.id.int().tolist()
                class_ids = results[0].boxes.cls.tolist()

                #annotated_frame = results[0].plot()
                annotated_frame = frame

                # Plot the tracks
                for box, track_id, class_id in zip(boxes, track_ids, class_ids):
                    x, y, w, h = box
                    area = w * h
                    area_int = round(area.item())
                    track_info = track_history[track_id]
                    object_class = model.names[int(class_id)]
                    distance = 0

                    # Append track history and area to the dictionary
                    track_info["track"].append((float(x), float(y)))  # x, y center point
                    track_info["area"].append(area_int)

                    # Retain track history and area for 150 frames
                    if len(track_info["track"]) > 40:
                        track_info["track"].pop(0)
                        track_info["area"].pop(0)

                #ADD CUSTOM CODE HERE BASED ON REQUIREMENTS

                # Display the annotated frame
                resized_frame = cv2.resize(annotated_frame, (1536, 864))
                cv2.imshow("YOLOv8 Tracking", resized_frame)


        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # break the loop if the end of the video is reached
        break
cap.release()
cv2.destroyAllWindows()
