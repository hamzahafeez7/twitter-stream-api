import os
from tweepy import OAuth1UserHandler, API, Stream
from tweepy import StreamRule
from twitter_client import Streaming
# from def_secrets import consumer_key, consumer_secret, access_key, access_secret
from dotenv import load_dotenv
load_dotenv()

bearer_token  = str(os.environ["BEARER_TOKEN"])
# consumer_key = os.environ["API_KEY"]
# consumer_secret = os.environ["API_KEY_SECRET"]
# access_token = os.environ["ACCESS_TOKEN"]
# access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]


def main():
    # auth = OAuth1UserHandler(
    #     consumer_key, consumer_secret, access_token, access_token_secret
    # )

    # api = API(auth)
    streamer = Streaming(bearer_token)    
    # streamer.add_rules(StreamRule("f1 OR (formula 1) OR formula1 lang:en"))
    streamer.add_rules(StreamRule("f1 OR formula1 lang:en"))

    try:
        streamer.filter()

    except Exception as err:
        print("Exception Raised - Error" + str(err))

if __name__ == "__main__":
    main()