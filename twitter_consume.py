import tweepy as tw
import pandas as pd
import utils as ut

FILE_PREFIX = "twitter_stream" 

# API key and API secret
my_api_key = "2T3RpBLMfFXUf7wguQadbyaQm"
my_api_secret = "EvASl3xUkp8KP5sgJjYe624rp1Iw8DJ4NCmsCHBhVe1iNuIjw7"


# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)


#Search query definition 
search_query = "#worldcup2022"


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
        text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
    except Exception as err:
        print("Error reading hashtags")
        print(err)
        pass

    tweets_df = tweets_df.append(pd.DataFrame({'user_name': tweet.user.name,
        'user_location': tweet.user.location,
        'user_description': tweet.user.description, 
        'user_verified': tweet.user.verified,
        'text': tweet.text, 
        'hastags': [hashtags if hashtags else None],
        'source': tweet.source}))
    tweets_df = tweets_df.reset_index(drop =True)

ut.df_to_csv(tweets_df, FILE_PREFIX)



# print(tweets_df.head())

