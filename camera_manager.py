import cv2

class CameraManager:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def capture(self):
        ret, frame = self.cap.read()
        if ret:
            cv2.imwrite("capture.jpg", frame)
            return "capture.jpg"