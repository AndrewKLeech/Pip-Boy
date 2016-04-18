from twitter import *


def showTweets(x, num):
    # display a number of new tweets and usernames
    for i in range(0, num):
        print(x[i]['user']['screen_name'])
        print(x[i]['text'])


def getTweets():
    # Put in token, token_key, con_secret, con_secret_key
    t = Twitter(
        auth=OAuth('', '',
                   '', ''))

    x = t.statuses.home_timeline(screen_name="AndrewKLeech")
    return x


numberOfTweets = 5

showTweets(getTweets(), numberOfTweets)
