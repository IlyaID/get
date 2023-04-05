import RPi.GPIO as GPIO
import time


DAC = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(DAC)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comparator = 4
weight = [128, 64, 32, 16, 8, 4, 2, 1]
LEDS = [24, 25, 8, 7, 12, 16, 20, 21]
LEDS1 = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)
GPIO.setup(LEDS, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LEDS1, GPIO.OUT, initial = GPIO.LOW)

def decimal2binary(value, n):
    return [int(element) for element in bin(value)[2:].zfill(n)]

#def num2dac(value):
   # signal = decimal2binary(value)
   # GPIO.output(DAC, signal)
   # return signal


def adc():
    summary = 0
    for value in range(8):
        signal = decimal2binary(summary + weight[value],8)
        GPIO.output(DAC, signal)
        time.sleep(0.01)
        comparatorValue = GPIO.input(comparator)
        if(comparatorValue == 1):
            summary += weight[value]
        signal = decimal2binary(summary,8)
        voltage = summary / levels * maxVoltage
        for value in range(8):
            if (value < summary / 255 * 8):
                GPIO.output(LEDS[value], 1)
            else:
                GPIO.output(LEDS[value], 0)
        print("Summary value = {:^3} -> {}, output voltage = {:.2f}".format(summary, signal, voltage))
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