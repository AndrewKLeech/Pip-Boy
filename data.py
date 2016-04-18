from twitter import *
from tkinter import *


def showTweets(x, num):
    # display a number of new tweets and usernames
    for i in range(0, num):
        line1 = (x[i]['user']['screen_name'])
        line2 = (x[i]['text'])
        w = Label(master, text=line1 + "\n" + line2)
        w.pack()

def getTweets():
    # Put in token, token_key, con_secret, con_secret_key
    t = Twitter(
        auth=OAuth('705153959368007680-F5OUf8pvmOlXku1b7gpJPSAToqzV4Fb', 'bEGLkUJBziLc17EuKLTAMio8ChmFxP9aHYADwRXnxDsoC',
                   'gYDgR8lcTGcVZS9ucuEIYsMuj', '1dwHsLDN2go3aleQ8Q2vcKRfLETc51ipsP8310ayizL2p3Ycii'))

    x = t.statuses.home_timeline(screen_name="AndrewKLeech")
    return x


numberOfTweets = 5



master = Tk()
showTweets(getTweets(), numberOfTweets)


mainloop()