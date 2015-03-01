import tweepy
from tweepy.api import API

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


class StdOutListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''
 
    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)
 
        # There are many options in the status object,
        # hashtags can be very easily accessed.
        for hashtag in status.entries['hashtags']:
            print(hashtag['text'])
 
        return true
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
 
if __name__ == '__main__':
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
 
#    stream1 = tweepy.Stream(auth, listener)
#    stream1.filter( track=['python'])
#    stream1.filter(follow=['15687368'], track=['#pythoncentral'])


class Stream2Screen(tweepy.StreamListener):
    def __init__(self, api=None):
        self.api = api or API()
        self.n = 0
        self.m = 20

    def on_status(self, status):
        print status.text.encode('utf8')
        self.n = self.n+1
        if self.n < self.m: return True
        else:
            print 'tweets = '+str(self.n)
            return False

stream = tweepy.streaming.Stream(auth, Stream2Screen())
stream.filter(track=['python'])
#    stream1.filter(follow=['15687368'], track=['#pythoncentral'])
