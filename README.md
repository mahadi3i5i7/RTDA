# RTDA - Real-Time Driving Assistant

RTDA is a real-time driving assistant system that leverages deep learning and object tracking to provide assistance to the driver of the host vehicle and make our roads safer.

The system utilizes a customized YOLOv8 model for real-time detection of objects in a live video stream. Object tracking is achieved through the ByteTrack algorithm over consecutive frames, enabling the system to obtain tracking IDs and bounding box data for each detected object. The information is used to track the position of objects over time and derive a closeness factor, which quantifies the rate of change in proximity of the object to the host vehicle. By using the object’s location in the frame along with the closeness factor, the system can assess the rate of approach of detected objects. Using this information, the system notifies and warns the driver of potential hazards in real-time.

## Files

- **Custom.py** - Python script for training YOLOv8 model on custom dataset
- **images_png_to_jpg.py** - Python script for converting images in dataset into jpg format
- **Tracking.py** - Detection, tracking, and driving assistance code (needs to be modified for every camera)
- **camera_calibration.py** - Python script for calibrating camera and driving zones
- **arduino_module.py** - Python script for serial communication and sending/receiving commands with Arduino
