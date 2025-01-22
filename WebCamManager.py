import cv2
from ultralytics import YOLO


class WebCamManager:
    def __init__(self, model_path, video_source=0):
        self.cap = cv2.VideoCapture(video_source)
        self.model = YOLO(model_path)
        self.detected_frames = 0  # Counter for consecutive detections

    def process_frame(self):
        success, frame = self.cap.read()
        if not success:
            return None

        results = self.model(frame)
        face_detected = False
        bottle_cup_detected = False

        if results:
            for result in results:
                boxes = result.boxes

                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)  # Bounding box coordinates
                    class_id = int(box.cls)  # Class ID
                    class_name = self.model.names[class_id]

                    # Draw the bounding box on the image
                    color = (0, 255, 0)  # Green color
                    thickness = 2  # Box line thickness
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)

                    # Add the class name next to the box
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(frame, class_name, (x1, y1 - 10), font, 0.9, color, thickness)

                    # Check for face and water cup
                    if class_name == 'face':
                        face_detected = True
                    elif class_name in ['water_bottle', 'water_cup']:
                        bottle_cup_detected = True

                # Increment counter if both detected
                if face_detected and bottle_cup_detected:
                    self.detected_frames += 1
                else:
                    self.detected_frames = 0

        # Return True if both detected for 50 consecutive frames
        if self.detected_frames >= 50:
            return True

        # Convert from BGR to RGB for Tkinter
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame

    def release(self):
        self.cap.release()