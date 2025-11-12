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

```
## Usage

This project can be used in two ways: via command line (script) or via Streamlit (web interface).

---

### 1. Run the face detection script directly (works in Colab/Kaggle)

You can use the core detection function in notebooks or scripts:
```python
take the function in face_detection.py
import cv2

# Load an image 
img = cv2.imread("your_image.jpg")

#Detect face
mp_det = mp.solutions.face_detection
with mp_det.FaceDetection(min_detection_confidence=0.5, model_selection=0) as fd:
    result = get_detections(img, fd)

# Save output
cv2.imwrite("output/output_image.png", result)
```
### 2. Run streamlit file (run.py) locally
