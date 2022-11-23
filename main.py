from tweepy import OAuthHandler, API, Stream
from twitter_listener import StreamListener
from secrets import consumer_key, consumer_secret, access_key, access_secret
from datetime import datetime
from utils import UTC

FILENAME = 'stream_listen_output_' + str(UTC) + '.csv'

if __name__ == "main":
    auth  = OAuthHandler(consumer_key, consumer_secret)
    auth.access_token(access_key, access_secret)

    api = API(auth)

    #Instantiate Stream Object
    streamListener = StreamListener()

    stream = Stream(auth = api.auth, listener = streamListener, tweet_mode = 'extended')

    with open('out.csv', 'w', encoding= 'utf-8') as f:
        f.write('date,user,is_retweet,is_quote,text,quoted_text\n')
    
    tags = ["hate speech"]
    stream.filter(track=tags)

