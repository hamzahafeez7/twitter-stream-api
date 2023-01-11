import os
import tweepy
import datetime
from config import stream_runtime, file_prefix, error_prefix
import pandas as pd
from utils import UTC
import logging

FILENAME = file_prefix + 'twitter_stream_' + str(UTC) + '.csv'
ERROR_LOG_FILENAME = error_prefix + 'errors_twitter_stream_' + str(UTC) + '.csv'
class Streaming(tweepy.StreamingClient):
    
    def __init__(self,*args, **kwargs):
        """
        Overriding constructor method to define time tracking variable
        stop_time - Time tracking for stream instance
        tweets_df - Pandas dataframe to hold and write streams to csv
        errors_df - Pandas dataframe to hold and write errors faced in streaming
        file_name - Filename for resultant file
        iterator - Tracking the number of tweets received
        """
        self.stop_time = datetime.datetime.now() + datetime.timedelta(minutes=int(stream_runtime))
        self.tweets_df = pd.DataFrame(columns=['created_at', 'id', 'text', 'author_id'])
        self.errors_df = pd.DataFrame(columns=['time_utc', 'error_code', 'error_message'])
        self.file_name = FILENAME
        self.iterator = 0
        super(Streaming, self).__init__(*args, **kwargs)
    
    def on_connect(self):
        print('Connected to Twitter Stream API.')

    def on_tweet(self, tweet):
        print("========Tweet Streamed=========")        
        print('Twitter ID: ' + str(tweet.id))
        print('Tweet:' + str(tweet.text))
        print('Created At:' + str(tweet.created_at))
        print('===============================')

        #Ensuring the stream runs for the specified time only
        if datetime.datetime.now() > self.stop_time:
            #Convert to CSV here
            self.tweets_df.to_csv(FILENAME)
            self.errors_df.to_csv(ERROR_LOG_FILENAME)
            print('Tweets saved to file:' + FILENAME)
            # print(self.tweets_df)
            raise Exception('Time Expired. Kindly restart the stream')
        else:
            tweet_data = {'created_at': tweet.created_at, 'id': tweet.id, 'text': tweet.text, 'author_id': tweet.author_id}
            self.tweets_df = self.tweets_df.append(tweet_data, ignore_index = True)            
            self.iterator += 1 

    def on_errors(self, errors):
        print("========Streaming Error=========")
        print('Error Code: ' + str(errors.code))
        print('Error Message: ' + str(errors.message))
        print("================================")
        error_data = {'time_utc': str(UTC), 'error_code': errors.code, 'text': errors.messages}
        self.errors_df = self.errors_df.append(error_data, ignore_index = True)
        print('Errors to be printed to file' + str(ERROR_LOG_FILENAME))



    

