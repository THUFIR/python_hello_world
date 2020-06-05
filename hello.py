import tweepy
import os

consumer_key=os.environ['twitter_consumer_key']
consumer_secret=os.environ['twitter_consumer_secret']
access_token=os.environ['twitter_access_token']
access_token_secret=os.environ['twitter_access_token_secret']


print(consumer_key)
print(consumer_secret)
print(access_token)
print(access_token_secret)




auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


