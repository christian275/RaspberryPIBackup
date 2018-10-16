import picamera
import datetime

x = str(datetime.datetime.now())

camera = picamera.PiCamera()
camera.resolution = (1080, 720)
camera.start_recording('/home/pi/Documents/Security Folder/Camera Captures/' + x + '.h264')
camera.wait_recording(15)
camera.stop_recording()
