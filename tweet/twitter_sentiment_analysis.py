import tweepy
from textblob import TextBlob
from twitter_credentials import con_key, con_secret, acc_token, acc_secret
from datetime import datetime
import json
import os
import csv
import sys


def file_write(msg, file_prefix="tweet_data"):
    now = datetime.now()
    str_dt = now.strftime("%Y%m%d%H")

    data_file_name = "~/" + file_prefix + "_" + str_dt + ".txt"

    if os.path.exists(os.path.expanduser(data_file_name)):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if not

    with open(os.path.expanduser(data_file_name), append_write) as fid:
        tweet_write = csv.writer(fid, delimiter=',', quotechar='"')
        tweet_write.writerow(msg)


def log_write(text, log_prefix="tweet_log"):
    now = datetime.now()
    str_dt = now.strftime("%Y%m%d")
    str_time = now.strftime("%H:%M")

    log_file_name = "~/" + log_prefix + "_" + str_dt + ".txt"

    if os.path.exists(os.path.expanduser(log_file_name)):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if not

    with open(os.path.expanduser(log_file_name), append_write) as fid:
        fid.write(str_time + " : " + text + "\n")


class TwitterStream(tweepy.StreamListener):

    def on_status(self, status):
        log_write(status.text, "tweet_stream_log")

    # disconnect the stream if we receive an error message indicating we are overloading Twitter
    def on_error(self, status_code):
        log_write(str(status_code), "tweet_stream_log")

        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False

    def on_data(self, data):
        now = datetime.now()
        all_data = json.loads(data)

        screen_name = all_data["user"]["screen_name"].encode('UTF-8')
        user_name = all_data["user"]["name"].encode('UTF-8')
        # create_dt = all_data["created_at"].encode('UTF-8')              #
        # user_loc = all_data["user"]["location"].encode('UTF-8')
        message = all_data["text"].encode('UTF-8')


        retweet = all_data["retweeted"]

        mins_now = int(now.strftime("%M"))
        mins_log = mins_now % 15

        if not retweet:
            file_write([screen_name,
                        user_name,
                        # create_dt,
                        # user_loc,
                        message], "tweet_stream")

        if mins_log == 0:
            log_write("Streaming data from twitter ....", "tweet_stream_log")

        return True


    class Tweet(object):

        def __init__(self):
            self.auth = tweepy.OAuthHandler(consumer_key=con_key, consumer_secret=con_secret)
            self.auth.set_access_token(acc_token, acc_secret)
            self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            self.tweet_stream = None
            self.stream_listener = None

        def create_twitter_stream(self):
            self.stream_listener = TwitterStream()
            self.tweet_stream = tweepy.Stream(auth=self.api.auth, listener=self.stream_listener)

        def filter_tweets(self, hashtags):
            if not self.tweet_stream:
                self.createTwitterStream()

            try:
                self.tweet_stream.filter(track=hashtags, languages=["en"])
            except Exception as ex:
                log_write(str(ex))
                self.tweet_stream.filter(track=hashtags, languages=["en"])

        def search_tweets(self, hashtags, num_tweets=1000):
            tweet_list = []
            last_id = -1  # id of last tweet seen
            loop_cnt = 0

            for hashtag in hashtags:
                while len(tweet_list) < num_tweets:
                    try:
                        tweet_list = self.api.search(q=hashtag, lang=["en"], count=500, max_id=str(last_id - 1))
                    except tweepy.TweepError as ex:
                        log_write(str(ex), "tweet_search_log")
                        break
                    else:
                        if not tweet_list:
                            log_write("Could not find any more tweets!", "tweet_search_log")
                            break
                        loop_cnt += 1
                        user_tweets = [[twt.user.screen_name.encode('utf8'),            # Screen name
                                        twt.user.name.encode('utf8'),                   # User name
                                        # twt.created_at.encode('UTF-8'),               # created at
                                        # twt.user.location,                            # location
                                        twt.text.encode('utf8'),                        # text
                                        ] for twt in tweet_list if not twt.retweeted]

                        file_write(user_tweets, "tweet_search" + str(loop_cnt))         # Write to file
                        last_id = tweet_list[-1].id



if __name__ == "__main__":
    tweet = Tweet()
    tweet.create_twitter_stream()

    print(sys.argv[1])
    if sys.argv[1] == "stream":
        hashtags = ["#usps",
                    "#ups",
                    "#fedex",
                    "#dhl",
                    "@upshelp",
                    "@fedexhelp",
                    "@uspshelp",
                    "@DHLUSHelp"
                    ]
        tweet.filter_tweets(hashtags)
    elif sys.argv[1] == "search":
        hashtags = ["#%23usps",
                    "#%23ups",
                    "#%23fedex",
                    "#%23dhl",
                    "#%40upshelp",
                    "#%40fedexhelp",
                    "#%40uspshelp",
                    "#%40DHLUSHelp"
                    ]
        tweet.search_tweets(hashtags, 10000)

