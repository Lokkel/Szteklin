from picamera import PiCamera
import datetime
from time import sleep
t = datetime.datetime.now()


camera = PiCamera()
camera.start_preview()
sleep(5)
p = '/home/pi/milan/Szteklin/picam/{}.jpg'.format(t)
p = p.replace(" ","_")


camera.capture(p)
#camera.annotate_text = time.time()
#camera.annotate_text_size = 50 # (values 6 to 160, default is 32)
#camera.annotate_text = dt.datetime.now().strftime('%A %d %b %Y %H:%M')
camera.stop_preview()
