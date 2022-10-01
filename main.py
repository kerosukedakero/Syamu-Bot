#コメントを追加
import syamu
import learn
import tweettest

with open("create.txt", "r") as f:
    s = f.read()

tweettest.tweet(s)
