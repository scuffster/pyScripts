#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "15695600-3nQptZFpwp6iDpeMSVUzKr7YFe0TbZDjaOwKF5XM1"
access_token_secret = "gHaGurhhHNGBS55HeRwhf7rOT64tNFtmtVjrwHI8Dwbmx"
consumer_key = "avdQlw4uYIgmj8XHW6RRxwSGb"
consumer_secret = "G3lL7eDUFX2CVjlD6jXFT6Wr6MWCjCcYLz6WzMRpEgEslL5ekl"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['tuberculosis', 'tb'])
    stream.filter(track=['scuffell'])
