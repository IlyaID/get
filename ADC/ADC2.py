import RPi.GPIO as GPIO
import time


DAC = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(DAC)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comparator = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)


def decimal2binary(value, n):
    return [int(element) for element in bin(value)[2:].zfill(n)]

#def num2dac(value):
   # signal = decimal2binary(value)
   # GPIO.output(DAC, signal)
   # return signal

def adc():
    for value in range(256):
            signal = decimal2binary(value, 8)
            GPIO.output(DAC, signal)
            time.sleep(0.01)
            voltage = value / levels * maxVoltage
            comparatorValue = GPIO.input(comparator)
            print(comparatorValue)
            #print("ADC value = {:^3} -> {}, output voltage = {:.2f}".format(value, signal, voltage))
            if comparatorValue == 0:
                print("ADC value = {:^3} -> {}, output voltage = {:.2f}".format(value, signal, voltage))
                break
try:
    while True:
        adc()
            
                
                

except ValueError:
    print('Please enter number from 0 to 255\n')

except KeyboardInterrupt:
    print('\n The program was stopped by the keyboard')  

finally:
    GPIO.output(DAC, GPIO.LOW)
    GPIO.cleanup()
    print('GPIO cleanup completed')