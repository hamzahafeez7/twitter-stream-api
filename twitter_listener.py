from tweepy import Stream
import sys

#Inheriting class from Tweepy.StreamListener and override (on_status, on_error) methods
class StreamListener(Stream):
    def on_status(self, status): 
        print(status.id_str)

        #Flagging tweets as retweet  in case "retweet_status" exists in tweet input
        is_retweet = hasattr(status, "retweeted_status")

        #Check for full text if extended tweet
        if hasattr(status, "extended_tweet"):
            text = status.extended_tweet['full_text']
        else:
            text = status.text

        # check if this is a quote tweet.
        is_quote = hasattr(status, "quoted_status")
        quoted_text = ""
        if is_quote:
            # check if quoted tweet's text has been truncated before recording it
            if hasattr(status.quoted_status,"extended_tweet"):
                quoted_text = status.quoted_status.extended_tweet["full_text"]
            else:
                quoted_text = status.quoted_status.text

        # remove characters that might cause problems with csv encoding
        remove_characters = [",","\n"]
        for c in remove_characters:
            text.replace(c," ")
            quoted_text.replace(c, " ")

        with open("out.csv", "a", encoding='utf-8') as f:
            f.write("%s,%s,%s,%s,%s,%s\n" % (status.created_at,status.user.screen_name,is_retweet,is_quote,text,quoted_text))

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()



        