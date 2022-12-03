import os
from tweepy import StreamingClient

class StreamingClient(StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.id)
        print(tweet.text)
        print('==========================')
    

