[app]

title = Ortographer
package.name = ortographer
package.domain = org.test

source.dir = .
source.include_exts = py,kv,png,jpg,json

version = 1.0.0

requirements = python3,kivy,pyjnius,bleak,opencv-python,numpy

android.api = 34
android.minapi = 24
android.arch = arm64-v8a

android.permissions = CAMERA, BLUETOOTH,BLUETOOTH_ADMIN,ACCESS_FINE_LOCATION,BLUETOOTH_CONNECT,BLUETOOTH_SCAN, WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

