from ScreenBlockManager import ScreenBlockManager
from WebCamManager import WebCamManager


class Main:
    def __init__(self, model_path):
        # Initializes the webcam and screen managers
        self.webcam_manager = WebCamManager(model_path)
        self.screen_manager = ScreenBlockManager(self.webcam_manager)

    def run(self):
        # Runs the screen blocking process
        self.screen_manager.create_black_screen()


if __name__ == "__main__":
    model_path = "/home/dandan/Documentos/estudos/drink_water/drink_water_yolo/runs/detect/train3/weights/best.pt"
    app = Main(model_path)
    app.run()