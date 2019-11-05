import RPi.GPIO as GPIO
from time import sleep, time, strftime, localtime
from datetime import *

def GrowLight(command ,StartTime=0, StopTime=0):
    GPIO.setmode(GPIO.BCM)
    light_relay = 23
    GPIO.setwarnings(False)
    GPIO.setup(light_relay, GPIO.OUT)
    if command:
        hour = int(strftime("%H", localtime())) 
        if hour in range(StartTime, StopTime+1):
            print("LED ON!!!")
            GPIO.output(light_relay, 0)
        else:
            print("LED OFF!!!")
            GPIO.output(light_relay, 1)
        return True
    else:
        GPIO.output(light_relay, 1)
        return False
    