from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock
from kivy.utils import platform

from ble_manager import BLEManager
from sensor_manager import SensorManager
from storage_manager import StorageManager
from camera_manager import CameraManager
from opencv_processor import OpenCVProcessor

if platform == "android":
    from android.permissions import request_permissions, Permission

class HomeScreen(Screen):
    pass

class CameraScreen(Screen):
    pass

class StorageScreen(Screen):
    pass


class OrtographerApp(App):

    heading = NumericProperty(0)
    ble_status = StringProperty("Disconnected")

    def build(self):

        if platform == "android":
            request_permissions([
                Permission.BLUETOOTH_SCAN,
                Permission.BLUETOOTH_CONNECT,
                Permission.ACCESS_FINE_LOCATION,
                Permission.CAMERA
            ])

        self.ble = BLEManager(self)
        self.sensor = SensorManager(self)
        self.storage = StorageManager()
        self.camera = CameraManager()
        self.processor = OpenCVProcessor()

        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(CameraScreen(name="camera"))
        sm.add_widget(StorageScreen(name="storage"))

        Clock.schedule_interval(self.update_heading, 0.1)

        return sm

    def update_heading(self, dt):
        self.heading = self.sensor.heading


if __name__ == "__main__":
    OrtographerApp().run()