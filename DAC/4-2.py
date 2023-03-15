import RPi.GPIO as GPIO
import time


def decimal2binary(value, n):
    return [int(element) for element in bin(value)[2:].zfill(n)]

GPIO.setmode(GPIO.BCM)
DAC = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(DAC, GPIO.OUT)

try:
    while(1):
        input_value = input('Please enter number \n')
        
        t = int(input_value)/256/2
        for i in range(256):
            GPIO.output(DAC, decimal2binary(i, 8))
            time.sleep(t)
        for i in range(256, -1, -1):
            GPIO.output(DAC, decimal2binary(i, 8))
            time.sleep(t)
                
        

except ValueError:
    print('Please enter number from 0 to 255\n')

except KeyboardInterrupt:
    print('done')  

finally:
    GPIO.output(DAC, GPIO.LOW)
    GPIO.cleanup(DAC)