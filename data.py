from twitter import *
from tkinter import *


def showTweets(x, num):
    # display a number of new tweets and usernames
    for i in range(0, num):
        line1 = (x[i]['user']['screen_name'])
        line2 = (x[i]['text'])
        w = Label(master, text=line1 + "\n" + line2 + "\n\n")
        w.pack()

def getTweets():

    x = t.statuses.home_timeline(screen_name="AndrewKLeech")
    return x


def tweet():

    global entryWidget

    if entryWidget.get().strip() == "":
        print("Empty")
    else:
        t.statuses.update(status=entryWidget.get().strip())
        entryWidget.delete(0,END)
        print("working")


# Put in token, token_key, con_secret, con_secret_key
t = Twitter(
    auth=OAuth('705153959368007680-F5OUf8pvmOlXku1b7gpJPSAToqzV4Fb', 'bEGLkUJBziLc17EuKLTAMio8ChmFxP9aHYADwRXnxDsoC',
               'gYDgR8lcTGcVZS9ucuEIYsMuj', '1dwHsLDN2go3aleQ8Q2vcKRfLETc51ipsP8310ayizL2p3Ycii'))

numberOfTweets = 5



master = Tk()
showTweets(getTweets(), numberOfTweets)

master.title("Tkinter Entry Widget")
master["padx"] = 40
master["pady"] = 20
# Create a text frame to hold the text Label and the Entry widget
textFrame = Frame(master)
#Create a Label in textFrame
entryLabel = Label(textFrame)
entryLabel["text"] = "Make a new Tweet:"
entryLabel.pack(side=LEFT)
# Create an Entry Widget in textFrame
entryWidget = Entry(textFrame)
entryWidget["width"] = 50
entryWidget.pack(side=LEFT)
textFrame.pack()
button = Button(master, text="Submit", command=tweet)
button.pack()

master.mainloop()