import os
from tweepy import OAuth1UserHandler, API, Stream
from tweepy import StreamRule
from twitter_client import Streaming
# from def_secrets import consumer_key, consumer_secret, access_key, access_secret
from dotenv import load_dotenv

load_dotenv()

bearer_token  = str(os.environ["BEARER_TOKEN"])


def main():

    streamer = Streaming(bearer_token)    
    streamer.add_rules(StreamRule("f1 OR formula1 lang:en"))

    try:
        streamer.filter()

    except Exception as err:
        print("Exception Raised - Error" + str(err))

if __name__ == "__main__":
    main()