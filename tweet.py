import twitter
import os
import time

consumer_key = os.environ['twitter_consumer_key']
consumer_secret = os.environ['twitter_consumer_secret']
access_token_key = os.environ['twitter_access_token_key']
access_token_secret = os.environ['twitter_access_token_secret']

api = twitter.Api(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token_key=access_token_key,
                    access_token_secret=access_token_secret)

tweet = f'@ankitsejwal The plants have been watered at ⏰{time.strftime("%H:%M")}'
api.PostUpdate(status=tweet)
