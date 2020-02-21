import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = "dcM0Jt2nNn11kZsIDIBuwZT9x"
consumer_secret = "QuTSPgi8kQO1enLuhdJykInj1QG5IAIyjZlGanPqhFaIBpFTlt"
access_token = '783636998905012224-9Kxvf7eUkCqDrfhVIsAlyfXBUSbD7Ci'
access_token_secret = 'bVNpFwWAHUEJ5owwzWtAEdpl3dsiDeiU26kUd6o5LEQZ7'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('lipaNaMpesa.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#DoMoreWithMPESA",count=200000,
                           lang="en",
                           since="2019-04-30").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.retweet_count, tweet.favorite_count, tweet.text.encode('utf-8')])


    #  retweeted in_reply_to_screen_name, name, screen_name,, 