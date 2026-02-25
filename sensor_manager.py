from jnius import autoclass, PythonJavaClass, java_method
from math import degrees
import numpy as np

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')
SensorManagerAndroid = autoclass('android.hardware.SensorManager')
Sensor = autoclass('android.hardware.Sensor')

class SensorListener(PythonJavaClass):
    __javainterfaces__ = ['android/hardware/SensorEventListener']
    __javacontext__ = 'app'

    def __init__(self, manager):
        super().__init__()
        self.manager = manager

    @java_method('(Landroid/hardware/SensorEvent;)V')
    def onSensorChanged(self, event):

        if event.sensor.getType() == Sensor.TYPE_ACCELEROMETER:
            self.manager.gravity = list(event.values)

        elif event.sensor.getType() == Sensor.TYPE_MAGNETIC_FIELD:
            self.manager.geomagnetic = list(event.values)

        if self.manager.gravity and self.manager.geomagnetic:

            R = [0] * 9
            I = [0] * 9

            success = SensorManagerAndroid.getRotationMatrix(
                R, I,
                self.manager.gravity,
                self.manager.geomagnetic
            )

            if success:
                orientation = [0] * 3
                SensorManagerAndroid.getOrientation(R, orientation)

                azimuth = degrees(orientation[0])
                azimuth = (azimuth + 360) % 360
                self.manager.heading = azimuth

    @java_method('(Landroid/hardware/Sensor;I)V')
    def onAccuracyChanged(self, sensor, accuracy):
        pass


class SensorManager:

    def __init__(self, app):
        self.heading = 0
        self.gravity = None
        self.geomagnetic = None

        activity = PythonActivity.mActivity
        manager = activity.getSystemService(Context.SENSOR_SERVICE)

        accelerometer = manager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)
        magnetometer = manager.getDefaultSensor(Sensor.TYPE_MAGNETIC_FIELD)

        self.listener = SensorListener(self)

        manager.registerListener(
            self.listener,
            accelerometer,
            SensorManagerAndroid.SENSOR_DELAY_UI
        )

        manager.registerListener(
            self.listener,
            magnetometer,
            SensorManagerAndroid.SENSOR_DELAY_UI
        )