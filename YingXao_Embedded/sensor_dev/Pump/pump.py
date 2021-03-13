import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pump_enable = 26

GPIO.setup(pump_enable, GPIO.OUT)

def turn_on():
    GPIO.output(pump_enable, 1)

def turn_off():
    GPIO.output(pump_enable, 0)

while True:
    status = input('On or Off? (1 or 0): ')
    if status == '1':
        try:
            turn_on()
        except:
            print('Failed to turn ON GPIO pin {}'.format(pump_enable))
    elif status == '0':
        try:    
            turn_off()
        except:
            print('Failed to turn OFF GPIO pin {}'.format(pump_enable))

