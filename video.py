from picamera import PiCamera
from time import sleep
import datetime


t = datetime.datetime.now()
p = '/home/pi/picam/{}.h264'.format(t)

p = p.replace(" ","_")
camera = PiCamera()
camera.start_preview()
sleep(3)
camera.start_recording(p)
sleep(10)
camera.stop_recording()
camera.stop_preview()
