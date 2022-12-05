import os
from tweepy import StreamingClient
import datetime
from config import EXEC_TIME_SECS

class StreamingClient(StreamingClient):
    
    def __init__(self):
        """Overriding constructor method to define time tracking variable"""
        self.stop_time = datetime.datetime.now() + datetime.timedelta(seconds=int(EXEC_TIME_SECS))
    
    def on_connect(self):
        print('Connected to Twitter Stream API.')

    def on_tweet(self, tweet):
        #Ensuring the stream runs for the specified time only
        print(tweet.id)
        print(tweet.text)
        print('==========================')

        if datetime.datetime.now() > self.stop_time:
            raise Exception('Time Expired. Kindly restart the stream')

    def on_errors(self, errors):
        print(errors)
    

