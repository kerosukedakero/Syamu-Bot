#coding: UTF-8

import twitter


def tweet(text):
    # 取得したキーとアクセストークンを設定する
    auth = twitter.OAuth(consumer_key="sll6YOCfP3cMXE25FAUOpmxbo",
                         consumer_secret="YGs04mf1qBtgaRoqYKTidBLZtyhKEmnfhTWft6RsM6zNYdFd9B",
                         token="1196066646944649216-qXiNg8bBHODv4RFxFe6ZzV9x4G79DZ",
                         token_secret="4bREwlrY7GN6GSc2f5AJzT3vTDCvBF0h3Wl1Cq0tgsBTs")

    t = twitter.Twitter(auth=auth)

    # twitterへメッセージを投稿する
    t.statuses.update(status=text)
