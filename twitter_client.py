import os
import tweepy
import datetime
from config import stream_runtime, file_prefix
import pandas as pd
from utils import UTC

FILENAME = file_prefix + 'twitter_stream_' + str(UTC) + '.csv'
class Streaming(tweepy.StreamingClient):
    
    def __init__(self,*args, **kwargs):
        """
        Overriding constructor method to define time tracking variable
        stop_time - Time tracking for stream instance
        tweets_df - Pandas dataframe to hold and write streams to csv
        file_name - Filename for resultant file
        iterator - To track the number of tweets received
        """
        self.stop_time = datetime.datetime.now() + datetime.timedelta(seconds=int(stream_runtime))
        self.tweets_df = pd.DataFrame(columns=['created_at', 'id', 'text', 'author_id'])
        self.file_name = FILENAME
        self.iterator = 0
        super(Streaming, self).__init__(*args, **kwargs)
    
    def on_connect(self):
        print('Connected to Twitter Stream API.')

    def on_tweet(self, tweet):
        
        # print(tweet.id)
        # print(tweet.text)
        # print(tweet.created_at)
        # print('==========================')

        #Ensuring the stream runs for the specified time only
        if datetime.datetime.now() > self.stop_time:
            #Convert to CSV here
            print(self.tweets_df)
            raise Exception('Time Expired. Kindly restart the stream')
        else:
            tweet_data = {'created_at': tweet.created_at, 'id': tweet.id, 'text': tweet.text, 'author_id': tweet.author_id}
            self.tweets_df = self.tweets_df.append(tweet_data, ignore_index = True)
            self.iterator += 1 
    # def on_errors(self, errors):
    #     print(errors)
    

