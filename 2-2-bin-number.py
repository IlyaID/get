import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
DAC = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(DAC, GPIO.OUT)
#number = [1, 0, 1, 0, 1, 0, 1, 0] 
#number = [0, 0, 0, 0, 0, 0, 1, 0]
number255 = [1, 1, 1, 1, 1, 1, 1, 1]
number127 = [0, 1, 1, 1, 1, 1, 1, 1]
number64 = [0, 1, 0, 0, 0, 0, 0, 0]
number32 = [0, 0, 1, 0, 0, 0, 0, 0]
number5 = [0, 0, 0, 0, 0, 1, 0, 1]
number0 = [0, 0, 0, 0, 0, 0, 0, 0]
number256 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
GPIO.output(DAC, number255)
time.sleep(15)
GPIO.output(DAC, GPIO.LOW)
time.sleep(1)
GPIO.output(DAC, number127)
time.sleep(15)
GPIO.output(DAC, GPIO.LOW)
time.sleep(1)
GPIO.output(DAC, number64)
time.sleep(15)
GPIO.output(DAC, GPIO.LOW)
time.sleep(1)
GPIO.output(DAC, number32)
time.sleep(15)
GPIO.output(DAC, GPIO.LOW)
time.sleep(1)
GPIO.output(DAC, number5)
time.sleep(15)
GPIO.output(DAC, GPIO.LOW)
time.sleep(1)
GPIO.output(DAC, number0)
time.sleep(15)
GPIO.output(DAC, GPIO.LOW)
time.sleep(1)
GPIO.output(DAC, number256)
time.sleep(15)
GPIO.output(DAC, GPIO.LOW)


GPIO.cleanup(DAC)