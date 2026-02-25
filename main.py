from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.utils import platform

# Android Permission Import
if platform == "android":
    from android.permissions import request_permissions, Permission


class HomeScreen(Screen):
    status = StringProperty("Permission not requested")


class OrtographerApp(App):

    def build(self):
        self.sm = ScreenManager()
        self.home = HomeScreen(name="home")
        self.sm.add_widget(self.home)

        # Permission erst nach Start der Activity anfragen
        if platform == "android":
            Clock.schedule_once(self.request_android_permissions, 1)

        return self.sm

    def request_android_permissions(self, dt):
        request_permissions(
            [Permission.CAMERA],
            self.permission_callback
        )

    def permission_callback(self, permissions, grants):
        if all(grants):
            self.home.status = "Camera Permission GRANTED"
        else:
            self.home.status = "Camera Permission DENIED"


if __name__ == "__main__":
    OrtographerApp().run()
