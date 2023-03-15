import RPi.GPIO as GPIO
import sys

def decimal2binary(value, n):
    return [int(element) for element in bin(value)[2:].zfill(n)]

GPIO.setmode(GPIO.BCM)
DAC = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(DAC, GPIO.OUT)

try:
    while(1):
        input_value = input('Please enter number from 0 to 255\n')
        if input_value == 'q': 
            sys.exit()
        elif input_value.isdigit() and 0 <= int(input_value) <= 255:
            GPIO.output(DAC, decimal2binary(int(input_value), 8))
            print("{:.4f}".format(int(input_value)/256*3.3))
        elif not input_value.isdigit():
            print('Please enter number from 0 to 255\n')

except ValueError:
    print('Please enter number from 0 to 255\n')

except KeyboardInterrupt:
    print('done')  

finally:
    GPIO.output(DAC, GPIO.LOW)
    GPIO.cleanup(DAC)