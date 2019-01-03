import RPi.GPIO as GPIO
import twitter
import os, time


def start_pump(duration):
    ''' run pump for a set interval '''

    GPIO.output(PUMP, GPIO.HIGH)
    time.sleep(duration)                   # keep pump running for 4 seconds
    GPIO.output(PUMP, GPIO.LOW)

def send_tweet(mention):
    
    consumer_key = os.environ['twitter_consumer_key']
    consumer_secret = os.environ['twitter_consumer_secret']
    access_token_key = os.environ['twitter_access_token_key']
    access_token_secret = os.environ['twitter_access_token_secret']

    api = twitter.Api(consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token_key=access_token_key,
                        access_token_secret=access_token_secret)

    tweet = f'@{mention} The plants have been watered at ⏰{time.strftime("%H:%M")}'
    
    # post tweet
    api.PostUpdate(status=tweet)


if __name__ == "__main__":

    PUMP = 17
    BUTTON = 18

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PUMP, GPIO.OUT)
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    # infinite loop
    while True:
        button_pressed = not GPIO.input(BUTTON)

        if button_pressed:
            start_pump(duration=4)                   # run pump for set interval time
            send_tweet(mention='ankitsejwal')       # mention username to tag people in tweet
        time.sleep(0.1)