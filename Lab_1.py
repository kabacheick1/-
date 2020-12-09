import RPi.GPIO as GPIO
import time

print ("initialization")
GPIO.setmode(GPIO.BOARD)

green_pin = 11
yellow_pin = 13
red_pin = 15
print ("Set green output to:", green_pin)
GPIO.setup(green_pin, GPIO.OUT)

try:
    while True:
        print ("Light green on")
        GPIO.output(green_pin, GPIO.HIGH)
        time.sleep(10)
        
        for a in range(6):
            GPIO.output(green_pin, GPIO.HIGH)
            time.sleep(0.5)

            GPIO.output(green_pin, GPIO.LOW)
            time.sleep(0.5)

        print ("Light green off")
        GPIO.output(green_pin, GPIO.LOW)
        time.sleep(2)

        print ("Light yellow on")
        GPIO.output(yellow_pin, GPIO.HIGH)
        time.sleep(4)

        print ("Light yellow off")
        GPIO.output(green_pin, GPIO.LOW)
        time.sleep(2)

        print ("Light red on")
        GPIO.output(green_pin, GPIO.HIGH)
        time.sleep(10)

        print ("Light red off")
        GPIO.output(green_pin, GPIO.LOW)
        time.sleep(2)

except KeyboardInterrupt:
    # pass
    GPIO.cleanup()
