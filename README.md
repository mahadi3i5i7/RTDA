# RTDA
RTDA is a real-time driving assistant system that leverages deep learning and object tracking to provide assistance to the driver of the host vehicle and make our roads safer. 
The system utilizes a customized YOLOv8 model for real-time detection of objects in a live video stream. 
Object tracking is achieved through ByteTrack algorithm over consecutive frames, enabling the system to obtain tracking IDs and bounding box data for each detected object. 
The information is used to track the position of objects over time and derive a closeness factor, which quantifies the rate of change in proximity of the object to the host vehicle. 
By using the object’s location in the frame along with closeness factor, the system can assess the rate of approach of detected objects. 
Using this information, the system notifies and warns the driver of potential hazards in real-time.

