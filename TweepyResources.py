import tweepy as tweepy
APY_KEY = "crRuaNqbQfq9DVNvroKxa1c3r"
API_Key_Secret = "ZNwVI1WeyHI2SW791IRv0eDXUyULaxXtrvztqwzO0IEYmglNPw"
consumer_key = "crRuaNqbQfq9DVNvroKxa1c3r"
consumer_secret = "ZNwVI1WeyHI2SW791IRv0eDXUyULaxXtrvztqwzO0IEYmglNPw"
access_token = "481365837-1t2frFX1RnuJQuIPaC1nVQZ72TwOTRzaQv03zrEF"
access_token_secret = "UGJfzsPk0SB2OAvMwSIkaRMJ3apCHWiux4fSsQ3favJf0"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


def get_twits_from_text(text_query):
    count = 500
    try:
        print(api.verify_credentials().screen_name)

        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.search_tweets, q=text_query).items(count)

        # Pulling information from tweets iterable object
        tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]

        # Creation of dataframe from tweets list
        # Add or remove columns as you remove tweet information
        tweets_df = pd.DataFrame(tweets_list)
        return tweets_df

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)