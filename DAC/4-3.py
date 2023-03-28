import RPi.GPIO as GPIO


def decimal2binary(value, n):
    return [int(element) for element in bin(value)[2:].zfill(n)]

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
pwm = GPIO.PWM(2, 1000)

pwm.start(0)



try:
    while(1):
        input_value = input('Please enter number\n')
        pwm.ChangeDutyCycle(int(input_value))
        print("{:.4f}".format(int(input_value)/100*3.3))
        
        
finally:
    GPIO.output(2, GPIO.LOW)
    
    GPIO.cleanup()