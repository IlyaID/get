import RPi.GPIO as GPIO
5


def decimal2binary(value, n):
    return [int(element) for element in bin(value)[2:].zfill(n)]

GPIO.setmode(GPIO.BCM)
DAC = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(DAC, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
pwm = GPIO.PWM(26, 25)
pwm.start(0)



try:
    while(1):
        input_value = input('Please enter number\n')
        pwm.ChangeDutyCycle(int(input_value))
        
finally:
    GPIO.output(DAC, GPIO.LOW)
    GPIO.cleanup(DAC)