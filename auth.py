import os
import tweepy

consumerKey = os.environ['API_KEY']
consumerSecret = os.environ['API_KEY_SECRET']
accessKey = os.environ['ACCESS_TOKEN']
accessSecret = os.environ['ACCESS_TOKEN_SECRET']

def print_auth():
    print(consumerKey)
    print(consumerSecret)
    print(accessKey)
    print(accessSecret)
    
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)