import os
from datetime import datetime
from kivy.utils import platform

if platform == "android":
    from android.storage import app_storage_path

class StorageManager:

    def __init__(self):
        if platform == "android":
            self.base_path = app_storage_path()
        else:
            self.base_path = "Ortographer"

        os.makedirs(self.base_path, exist_ok=True)

    def create_project(self, name):
        path = os.path.join(self.base_path, name)
        os.makedirs(path, exist_ok=True)
        return path

    def save_image(self, project, image_path):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_path = os.path.join(self.base_path, project, f"{timestamp}.jpg")
        os.rename(image_path, new_path)
        return new_path