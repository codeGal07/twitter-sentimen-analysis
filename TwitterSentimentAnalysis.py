import tweepy as tweepy
import csv
import datetime


def get_twitter_data(username, startDate, endDate):
    # twitter stuff
    # you get it from https://developer.twitter.com/
    consumerKey = "****"
    consumerSecret = "****"
    accessToken = "****"
    accessTokenSecret = "****"

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    alltweets = []
    outtweets = []

    tweets = api.user_timeline(screen_name=username, tweet_mode='extended', count=200)
    alltweets.extend(tweets)

    for tweet in alltweets:

        # so it's done because of the format to compare dates
        datumTvitaString = tweet.created_at.strftime('%Y-%m-%d %H:%M:%S')
        datumTvita = datetime.datetime.strptime(datumTvitaString, '%Y-%m-%d %H:%M:%S')

        # check if tweet is between start and end date
        if (datumTvita < endDate and datumTvita > startDate):
            # get retweets and tweets full text
            try:
                outtweets.append([tweet.id_str, tweet.created_at, tweet.retweeted_status.full_text])
            except:
                try:
                    outtweets.append([tweet.id_str, tweet.created_at, tweet.full_text])
                except:
                    continue

    # generate and write data in csv
    with open(f'{username}_tweets.csv', 'w') as f:
        f.write("%s__;_%s__;_%s\n" % ("id", "date", "text"))
        for tweet in outtweets:
            f.write("%s__;_%s__;_%s\n" % (tweet[0], tweet[1], tweet[2].encode("utf-8")))
    pass


def main():
    startDate = datetime.datetime(2020, 6, 1, 0, 0, 0)
    endDate = datetime.datetime(2021, 1, 1, 0, 0, 0)
    # generates csv file for this user between startDate and endDate
    get_twitter_data("BlazPlestenjak", startDate, endDate)


if __name__ == "__main__":
    main()
