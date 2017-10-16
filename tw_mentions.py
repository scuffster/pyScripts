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

api = tweepy.API(auth)
# get latest tweet for treats
f = open('latestTreatTweetId')
latestTreatTweetId = f.readline() 
#print 'latestTreatTweetId var contains: ', latestTreatTweetId 
f.close()

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
    #print tweet.text


user_tweets = api.mentions_timeline()
#user_tweets = api.mentions_timeline(since_id=latestTreatTweetId)
for tweet in user_tweets:
    print 'tweet.id is: ',tweet.id
    print 'latestTreatTweetId is: ',latestTreatTweetId
    if int(tweet.id) > int(latestTreatTweetId): 
       print 'latestTreatTweetId is: ',latestTreatTweetId
       latestTreatTweetId = tweet.id
    if tweet.text.find('moretreats') > -1:
       dispenseTreat = True
    print tweet.id, tweet.text,tweet.created_at,'from: @',  tweet.user.screen_name
f = open('latestTreatTweetId','w')
f.write(str(latestTreatTweetId))
f.close()
