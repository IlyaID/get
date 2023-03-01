import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LEDS = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(LEDS, GPIO.OUT)
AUX = [22, 23, 27, 18, 15, 14, 3, 2]
GPIO.setup(AUX, GPIO.IN)
#GPIO.setup(17,GPIO.IN)
#j = GPIO.input(17)
while 1:
    for i in range(8):
       GPIO.output(LEDS[i],GPIO.input(AUX[i]))
       j = GPIO.input(17)
     
    

GPIO.output(LEDS, GPIO.LOW)
GPIO.cleanup()