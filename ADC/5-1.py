import RPi.GPIO as GPIO
import time
import sys



DAC = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(DAC)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(co)

def decimal2binary(value, n):
    return [int(element) for element in bin(value)[2:].zfill(n)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(DAC, signal)
    return signal 

try:
    while True:
        input_value = input('Please enter value between 0 and 255 ("q" to exit) > \n')
        if input_value.isdigit():
            value = int(input_value)

            if value > levels - 1:
                print("The value is too large, try again")
                continue

            signal = num2dac(value)
            voltage = value / levels * maxVoltage
            print("Entered value = {:^3} -> {}, output voltage = {:.2f}".format(value, signal, voltage))

        elif input_value == 'q': 
            break

        else:
            print("Enter a positive integer")
            continue
                
        

except ValueError:
    print('Please enter number from 0 to 255\n')

except KeyboardInterrupt:
    print('\m The program was stopped by the keyboard')  

finally:
    GPIO.output(DAC, GPIO.LOW)
    GPIO.cleanup(DAC)
    print('GPIO cleanup completed')