import RPi.GPIO as GPIO
import time

LED = 11
CLAP = 40 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(CLAP,GPIO.IN)


clap = False
while True:
	if  GPIO.input(CLAP)
		clap = not clap
		GPIO.output(LED,clap)
		print("Switch ON" if clap else "Switch OFF")
		time.sleep(.5)

try: 
    except KeyboardInterrupt:
        print("Done")
        GPIO.cleanup()
	printf("Cleaning up")			

