import os
import tweepy

consumerKey = os.environ['API_KEY']
consumerSecret = os.environ['API_KEY_SECRET']
accessToken = os.environ['ACCESS_TOKEN']
accessTokenSecret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuth1UserHandler(
       consumerKey,
       consumerSecret,
       accessToken,
       accessTokenSecret
    )

api = tweepy.API(auth)
