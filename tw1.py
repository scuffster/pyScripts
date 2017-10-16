import tweepy
 
# Consumer keys and access tokens, used for OAuth
# Your twitter API credentials
consumer_key = '<>replace this'
consumer_secret = '<replace this>'
access_token = '<replace his>'
access_token_secret = '<replace this>'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status
api.update_status('Hello Python Central!')
