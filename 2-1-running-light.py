import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
LEDS = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(LEDS, GPIO.OUT)

for i in range(1,4):
    GPIO.output(21, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(25, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(24, GPIO.LOW)

GPIO.output(LEDS, GPIO.LOW)
GPIO.cleanup(LEDS)