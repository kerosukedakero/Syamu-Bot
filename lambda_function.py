import requests
import os
import syamu
import learn
import tweettest
import tweepy

def lambda_handler(event, context):
    with open("create.txt", "r") as f:
        s = f.read()

    tweettest.tweet(s)
    print('success')
