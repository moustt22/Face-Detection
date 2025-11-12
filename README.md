# Face-Detection
This project implements a real-time face detection system using Mediapipe and OpenCV. It can detect and track faces from live webcam feed, images, or video files, highlighting facial landmarks for easy visualization. The project is modular, easy to run, and includes example outputs to showcase detection results. 

## Features
- Detect faces in images and videos and live webcam
- Highlight detected faces with bounding boxes.
- Download output images/videos for further analysis.
- Easy-to-use command-line interface.

## Folder Structure
```text
face-detection-project/
│
├─ face_detection.py    # Core face detection logic
├─ run.py               # Streamlit web interface         
├─ processed_image.png  #output image example
├─ processed_video.mp4  #output video example
├─ README.md         # This file
