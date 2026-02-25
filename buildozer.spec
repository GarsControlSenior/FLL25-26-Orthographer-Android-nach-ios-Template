[app]

title = Ortographer
package.name = ortographer
package.domain = org.fll

source.dir = .
source.include_exts = py,kv,png,jpg,json

requirements = python3,kivy,pyjnius,bleak,opencv-python,numpy

android.api = 34
android.minapi = 24
android.arch = arm64-v8a

android.permissions = \
    BLUETOOTH_SCAN, \
    BLUETOOTH_CONNECT, \
    ACCESS_FINE_LOCATION, \
    CAMERA