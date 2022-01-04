import tweepy as tweepy
import csv
import datetime
import pandas as pd


def get_twitter_data(username, startDate, endDate):
    # twitter stuff
    # you get it from https://developer.twitter.com/
    consumerKey = "yourkeyhere"
    consumerSecret = "yourkeyhere"
    accessToken = "yourkeyhere"
    accessTokenSecret = "yourkeyhere"

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


def edit_text(text):
    text = text.replace("\xf0\x9f\x98\x80", "happy ")
    text = text.replace("\xf0\x9f\x98\x87", "smile ")
    text = text.replace("\xF0\x9F\x98\x88", "evil happy ")
    text = text.replace("\xF0\x9F\x98\x8E", "cool ")
    text = text.replace("\xF0\x9F\x98\x90", "neutral ")
    text = text.replace("\xF0\x9F\x98\x91", "expressionless ")
    text = text.replace("\xF0\x9F\x98\x95", "confused ")
    text = text.replace("\xF0\x9F\x98\x97", "kissing ")
    text = text.replace("\xF0\x9F\x98\x99", "kissing ")
    text = text.replace("\xF0\x9F\x98\x9B", "funny ")
    text = text.replace("\xF0\x9F\x98\x9F", "worried ")
    text = text.replace("\xF0\x9F\x98\xA6", "frowning ")
    text = text.replace("\xF0\x9F\x98\xA7", "anguished ")
    text = text.replace("\xF0\x9F\x98\xAC", "grimacing ")
    text = text.replace("\xF0\x9F\x98\xAE", "shoked ")
    text = text.replace("\xF0\x9F\x98\xAF", "hushed ")
    text = text.replace("\xF0\x9F\x98\xB4", "sleeping ")
    text = text.replace("\xF0\x9F\x98\xB6", "silent ")
    text = text.replace("\xF0\x9F\x98\x81", "smile ")
    text = text.replace("\xF0\x9F\x98\x82", "hilarious ")
    text = text.replace("\xF0\x9F\x98\x83", "happy ")
    text = text.replace("\xF0\x9F\x98\x84", "happy ")
    text = text.replace("\xF0\x9F\x98\x85", "happy Sweat ")
    text = text.replace("\xF0\x9F\x98\x86", "grinning ")
    text = text.replace("\xF0\x9F\x98\x89", "wink happy ")
    text = text.replace("\xF0\x9F\x98\x8A", "smiling ")
    text = text.replace("\xF0\x9F\x98\x8B", "savouring  ")
    text = text.replace("\xF0\x9F\x98\x8C", "relieved ")
    text = text.replace("\xF0\x9F\x98\x8D", "love ")
    text = text.replace("\xF0\x9F\x98\x8F", "smirking ")
    text = text.replace("\xF0\x9F\x98\x92", "unamused ")
    text = text.replace("\xF0\x9F\x98\x93", "hard work ")
    text = text.replace("\xF0\x9F\x98\x94", "sad ")
    text = text.replace("\xF0\x9F\x98\x96", "confounded ")
    text = text.replace("\xF0\x9F\x98\x98", "kissing love ")
    text = text.replace("\xF0\x9F\x98\x9A", "kiss ")
    text = text.replace("\xF0\x9F\x98\x9C", "joking ")
    text = text.replace("\xF0\x9F\x98\x9D", "joking ")
    text = text.replace("\xF0\x9F\x98\x9E", "disappointed ")
    text = text.replace("\xF0\x9F\x98\xA0", "angry ")
    text = text.replace("\xF0\x9F\x98\xA1", "furious ")
    text = text.replace("\xF0\x9F\x98\xA2", "crying ")
    text = text.replace("\xF0\x9F\x98\xA3", "helpless ")
    text = text.replace("\xF0\x9F\x98\xA4", "frustrated ")
    text = text.replace("\xF0\x9F\x98\xA5", "disappointed ")
    text = text.replace("\xF0\x9F\x98\xA8", "fearful ")
    text = text.replace("\xF0\x9F\x98\xA9", "weary ")
    text = text.replace("\xF0\x9F\x98\xAA", "sleepy ")
    text = text.replace("\xF0\x9F\x98\xAB", "tired ")
    text = text.replace("\xF0\x9F\x98\xAD", "crying ")
    text = text.replace("\xF0\x9F\x98\xB0", "nervous ")
    text = text.replace("\xF0\x9F\x98\xB1", "screaming ")
    text = text.replace("\xF0\x9F\x98\xB2", "astonished ")
    text = text.replace("\xF0\x9F\x98\xB3", "flushed ")
    text = text.replace("\xF0\x9F\x98\xB5", "dizzy ")
    text = text.replace("\xF0\x9F\x98\xB7", "mask ")

    return text


def interate_data(username):
    editedTweets = []
    data = pd.read_csv(username + "_tweets.csv", sep='__;_', engine='python')
    for i in range(len(data.text)):
        editedTweets.append([data.id[i], data.date[i], edit_text(data.text[i])])


def main():
    startDate = datetime.datetime(2020, 6, 1, 0, 0, 0)
    endDate = datetime.datetime(2021, 1, 1, 0, 0, 0)
    username = "BlazPlestenjak"
    # generates csv file for this user between startDate and endDate
    get_twitter_data(username, startDate, endDate)
    interate_data(username)


if __name__ == "__main__":
    main()
