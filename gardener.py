import RPi.GPIO as GPIO
import time

# pin configurations
LED_PIN = 1

class Gardener(object):

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(LED_PIN, GPIO.OUT)

    def set_led(self, value):
        ''' Turn LED on/off '''
        GPIO.output(LED_PIN, value)