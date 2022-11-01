from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (640, 480)  # sets camera resolution
camera.vflip = False  # Flip camera if necessary
camera.hflip = False  # Flip horizontally

camera.start_preview()
# displays camera on to the screen if you're plugged in to a display
time.sleep(2)  # sleeps camera for a moment to prevent issues

# to take a photo, use the following
# camera.capture("filename.jpg")

camera.start_recording("filename.h264")  # starts recording
time.sleep(10)  # how long in seconds
camera.stop_recording()  # stops recording
