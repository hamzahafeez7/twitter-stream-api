import tweepy as tw
import pandas as pd
from datetime import datetime

UTC = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
FILENAME = "twitter_stream_" + str(UTC) + ".csv"

# API key and API secret
my_api_key = "2T3RpBLMfFXUf7wguQadbyaQm"
my_api_secret = "EvASl3xUkp8KP5sgJjYe624rp1Iw8DJ4NCmsCHBhVe1iNuIjw7"


# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)


#Search query definition 
search_query = "#worldcup2022 -filter:retweets"


tweets= tw.Cursor(api.search_tweets, q=search_query, lang='en', since='2022-11-12').items(50)

tweets_list = []

for tweet in tweets:
    tweets_list.append(tweet)


print("Tweets Count:" + str(len(tweets_list)))

print(tweets_list[0])



tweets_df = pd.DataFrame()

for tweet in tweets_list:
    hashtags = []

    try:
        for hashtag in tweet.entities["hashtags"]:
            hashtag.append(hashtag['text'])
        text = api.get_status(id=tweet.id, tweet_mode = 'extended').full_text
    except:
        print("Error reading hashtags")
        pass

    tweets_df = tweets_df.append(pd.DataFrame({'user_name': tweet.user.name,
        'user_location': tweet.user.location,
        'user_description': tweet.user.description, 
        'user_verified': tweet.user.verified,
        'text': text, 
        'hastags': [hashtags if hashtags else None],
        'source': tweet.source}))
    tweets_df = tweets_df.reset_index(drop =True)

# print(tweets_df.head())

try:
    tweets_df.to_csv(FILENAME)
    print("Twitter feed written to file" + str(FILENAME))
except Exception as error:
    print("Unable to write dataframe to CSV ")
    print(error)