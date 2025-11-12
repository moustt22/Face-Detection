import cv2
import mediapipe as mp

mp_det = mp.solutions.face_detection

#Main Function to get detection and make a bounding box
def get_detections(img, fd):
    output = fd.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    H, W, _ = img.shape

    if output.detections:
        for detection in output.detections:
            box = detection.location_data.relative_bounding_box
            x, y, w, h = box.xmin, box.ymin, box.width, box.height

            x1, y1 = int(x * W), int(y * H)
            x2, y2 = int((x + w) * W), int((y + h) * H)

            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    return img

