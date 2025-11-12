import streamlit as st
import cv2
import mediapipe as mp
from PIL import Image
import numpy as np
import tempfile
from face_detection import get_detections

mp_det = mp.solutions.face_detection
st.title("Face Detection App")

option = st.radio("Choose input type:", ("Webcam", "Upload Image", "Upload Video"))

# ---------- Webcam ----------
if option == "Webcam":
    run = st.checkbox("Start Webcam")
    stframe = st.empty()
    webcam = cv2.VideoCapture(0)
    with mp_det.FaceDetection(min_detection_confidence=0.5, model_selection=0) as fd:
        while run:
            ret, frame = webcam.read()
            if not ret:
                break
            frame = get_detections(frame, fd)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(frame, channels="RGB")
    webcam.release()

# ---------- Image ----------
elif option == "Upload Image":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        with mp_det.FaceDetection(min_detection_confidence=0.5, model_selection=0) as fd:
            result = get_detections(img_cv, fd)
            result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
            st.image(result_rgb, channels="RGB")

            # Download button
            _, buffer = cv2.imencode(".png", result)
            st.download_button(
                label="Download Processed Image",
                data=buffer.tobytes(),
                file_name="processed_image.png",
                mime="image/png"
            )

# ---------- Video ----------
elif option == "Upload Video":
    uploaded_file = st.file_uploader("Choose a video...", type=["mp4","mov"])
    if uploaded_file:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())

        cap = cv2.VideoCapture(tfile.name)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(temp_output.name, fourcc, fps, (width, height))

        with mp_det.FaceDetection(min_detection_confidence=0.5, model_selection=1) as fd:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                frame = get_detections(frame, fd)
                out.write(frame)

        cap.release()
        out.release()
        # Download processed video
        with open(temp_output.name, "rb") as f:
            st.download_button(
                label="Download Processed Video",
                data=f,
                file_name="processed_video.mp4",
                mime="video/mp4"
            )
