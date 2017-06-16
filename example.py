from kellerLD import KellerLD
import time

sensor = KellerLD()
sensor.init()

print "Testing Keller LD series pressure sensor"
print "Press Ctrl + C to quit"
time.sleep(3)

while True:
	try:
		sensor.read()
		print("pressure: %7.4f bar\ttemperature: %0.2f C") % (sensor.pressure(), sensor.temperature())
		time.sleep(0.2)
	except Exception as e:
		print e
