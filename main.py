from tweepy import OAuthHandler, API, Stream
from twitter_listener import StreamListener
from def_secrets import consumer_key, consumer_secret, access_key, access_secret
from utils import UTC

FILENAME = 'stream_listen_output_' + str(UTC) + '.csv'

def main():
    print('Started Main Def')
    auth  = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = API(auth)

    #Instantiate Stream Object
    streamListener = StreamListener()

    stream = Stream(auth = api.auth, listener = streamListener, tweet_mode = 'extended')

    with open('out.csv', 'w', encoding= 'utf-8') as f:
        f.write('date,user,is_retweet,is_quote,text,quoted_text\n')
        print('Writing data into output stream')
    
    tags = ["fifa worldcup 2022"]


    try:
        stream.filter(track=tags)
    except Exception as err:
        print('Failed to run stream')
        print(err)
    print('End of business')


if __name__ == "__main__":
    main()

