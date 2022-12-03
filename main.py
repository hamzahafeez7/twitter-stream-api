import os
# from tweepy import OAuthHandler, API, Stream
# from twitter_listener import StreamListener
from tweepy import StreamRule
from twitter_client import StreamingClient
from def_secrets import consumer_key, consumer_secret, access_key, access_secret
from utils import UTC
from dotenv import load_dotenv

FILENAME = 'stream_listen_output_' + str(UTC) + '.csv'
load_dotenv()
bearer_token  = os.environ["BEARER_TOKEN"]

# consumer_key = os.environ["API_KEY"]
# consumer_secret = os.environ["API_KEY_SECRET"]
# access_token = os.environ["ACCESS_TOKEN"]
# access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]


def main():
    streamer = StreamingClient(bearer_token)
    streamer.add_rules(StreamRule("(formula 1) OR f1 OR formula1 lang:en"))

    try:
        streamer.filter()
    except Exception as err:
        print("Exception Raised - Error" + str(err))


if __name__ == "__main__":
    main()

