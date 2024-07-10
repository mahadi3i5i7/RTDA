import cv2
import numpy as np

# Open the camera
cap = cv2.VideoCapture(2)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    quit()

# Define trapezoid vertices and colors
trapezoid_warning = np.array([
    [990, 750],  # Top-left pixel
    [1030, 750],  # Top-right pixel
    [1560, 1200],  # Bottom-right pixel
    [400, 1200]  # Bottom-left pixel
], np.int32)
trapezoid_warning = trapezoid_warning.reshape((-1, 1, 2))
trapezoid_warning_color = (0, 200, 250)

trapezoid_braking = np.array([
    [940, 840],  # Top-left pixel
    [1080, 840],  # Top-right pixel
    [1400, 1100],  # Bottom-right pixel
    [560, 1100]  # Bottom-left pixel
], np.int32)
trapezoid_braking = trapezoid_braking.reshape((-1, 1, 2))
trapezoid_braking_color = (60, 0, 240)

trapezoid_slowspeed = np.array([
    [720, 990],  # Top-left pixel
    [1270, 990],  # Top-right pixel
    [1380, 1100],  # Bottom-right pixel
    [580, 1100]  # Bottom-left pixel
], np.int32)
trapezoid_slowspeed = trapezoid_slowspeed.reshape((-1, 1, 2))
trapezoid_slowspeed_color = (214, 186, 145)

# Read and display frames from the camera
while True:
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("Error: Could not read frame.")
        break

    # Draw trapezoids on the frame
    cv2.polylines(frame, [trapezoid_warning], isClosed=True, color=trapezoid_warning_color, thickness=2)
    cv2.polylines(frame, [trapezoid_braking], isClosed=True, color=trapezoid_braking_color, thickness=2)
    cv2.polylines(frame, [trapezoid_slowspeed], isClosed=True, color=trapezoid_slowspeed_color, thickness=2)

    # Draw number line
    cv2.line(frame, (0, frame.shape[0] - 100), (frame.shape[1], frame.shape[0] - 100), color=(255, 255, 255), thickness=2)
    for i in range(0, frame.shape[1], 100):
        cv2.putText(frame, str(i), (i, frame.shape[0] - 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.circle(frame, (i, frame.shape[0] - 100), 5, (0, 0, 250), -1)

    # Draw number line
    cv2.line(frame, (0, frame.shape[0] - 300), (frame.shape[1], frame.shape[0] - 300), color=(255, 255, 255), thickness=2)
    for i in range(0, frame.shape[1], 100):
        cv2.putText(frame, str(i), (i, frame.shape[0] - 280), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.circle(frame, (i, frame.shape[0] - 300), 5, (0, 0, 250), -1)

    # Resize the frame
    resized_frame = cv2.resize(frame, (1280, 720))

    # Display the resized frame
    cv2.imshow("Webcam", resized_frame)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
