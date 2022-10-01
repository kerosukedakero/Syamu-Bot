# coding: UTF-8
import tweepy
import csv
import re

consumer_key="sll6YOCfP3cMXE25FAUOpmxbo"
consumer_secret = "YGs04mf1qBtgaRoqYKTidBLZtyhKEmnfhTWft6RsM6zNYdFd9B"
access_key= "1196066646944649216-qXiNg8bBHODv4RFxFe6ZzV9x4G79DZ"
access_secret = "4bREwlrY7GN6GSc2f5AJzT3vTDCvBF0h3Wl1Cq0tgsBTs"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

q = "syamu" #キーワード
count=300

tweet_list=[]

tweets = api.search(q=q, locale="ja", count=count,tweet_mode='extended')
for tweet in tweets:
    tweet_list.append([tweet.full_text])

s = str(tweet_list)

s = s.replace("RT", "")

s = s.replace("[", "")

s = s.replace("]", "")

s = s.replace(r'\n', "\n")

s = s.replace("'", "")

s = s.replace(",", "")

s = s.replace("u3000", "")

s = s.replace("u200d", "")

for i in range(1000):

    s = s.replace("\\", "")

    s = s.replace("質問箱 #匿名質問募集中", "")

    s = s.replace("みんなからの匿名質問を募集中！こんな質問に答えてるよ", "")

    s = s.replace("●", "")
    
    s = s.replace("#", " #")

    s = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", s)

    s = re.sub('@.+?\s', "", s)
    
    s = re.sub(r'参戦ID:\w*', '', s)
#https://teratail.com/questions/200916

with open("tweetsdata.txt", "w") as f:
    f.write(s)
