from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.utils import platform


class HomeScreen(Screen):
    status = StringProperty("Waiting for permission...")


class OrtographerApp(App):

    def build(self):
        self.sm = ScreenManager()
        self.home = HomeScreen(name="home")
        self.sm.add_widget(self.home)

        if platform == "android":
            Clock.schedule_once(self.ask_permission, 0.8)

        return self.sm

    def ask_permission(self, dt):
        from android.permissions import request_permissions, Permission

        request_permissions(
            [Permission.CAMERA],
            self.permission_callback
        )

    def permission_callback(self, permissions, grants):
        if all(grants):
            self.home.status = "Camera permission granted"
        else:
            self.home.status = "Camera permission denied"


if __name__ == "__main__":
    OrtographerApp().run()
