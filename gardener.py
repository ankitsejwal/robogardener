import RPi.GPIO as GPIO
import twitter
import os, sys
from time import sleep, strftime


def start_pump(duration):
    ''' run pump for a set interval '''

    GPIO.output(PUMP, PUMP_ON)
    sleep(duration)                                 # keep pump running for set interval
    GPIO.output(PUMP, PUMP_OFF)


def send_tweet(mention):
    
    consumer_key = os.environ['twitter_consumer_key']
    consumer_secret = os.environ['twitter_consumer_secret']
    access_token_key = os.environ['twitter_access_token_key']
    access_token_secret = os.environ['twitter_access_token_secret']

    api =   twitter.Api(consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token_key=access_token_key,
                        access_token_secret=access_token_secret)

    tweet = '@{0} The plants have been watered at ⏰{1}'.format(mention, strftime("%H:%M:%S"))
    
    # post tweet
    api.PostUpdate(status=tweet)


def water_plants():
    print('Watering plants at {0}'.format(strftime("%H:%M:%S")))
    start_pump(duration=4)                          # run pump for set interval time
    send_tweet(mention='ankitsejwal')               # mention username to tag people in tweet

if __name__ == "__main__":

    PUMP = 17
    BUTTON = 18

    PUMP_ON = 0
    PUMP_OFF = 1

    WATERING_TIME = '16:00'

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PUMP, GPIO.OUT)
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.output(PUMP, PUMP_OFF)                     # initial state

    print('Program started successfully ...\n')

    try:
        # infinite loop
        while True:
            button_pressed = not GPIO.input(BUTTON)

            # water plants when button is pressed
            if button_pressed:
                water_plants()

            # water plants at a fixed time everyday
            if strftime('%H:%M') == WATERING_TIME:
                water_plants()
                sleep(60)                               # sleep for a minute                           

            sleep(0.2)                                  # slight delay in while loop
    except KeyboardInterrupt:
        sys.exit('\nProgram stopped successfully.')
