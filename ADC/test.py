import RPi.GPIO as GPIO
import time


def decimal2binary(value, n):
    return [int(element) for element in bin(value)[2:].zfill(n)]
input_value = input('Please enter number \n')

print("{:.4f}".format(int(input_value)/8*3.3))
