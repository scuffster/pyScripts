import tweepy
 
# Consumer keys and access tokens, used for OAuth
# Your twitter API credentials
consumer_key = 'VgyGLusD9rYL0yuctLbsYyv0L'
consumer_secret = 'dxoPSmbF3ap9CPAnWSd6UePCSRiIiOczOEsC6XSgWsPehBf6F4'
access_token = '15687368-uhUTmkQjrYTw8Vm7Hl9BxAxRJ6Mr5IZGgFYo1c1Ax'
access_token_secret = 'BJw4WdGTurY6WjZ9qtFcNiZ4uYItva5Rz7G9KkxBurGsA'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status
api.update_status('Hello Python Central!')
