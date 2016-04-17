from twitter import *

#Put in token, token_key, con_secret, con_secret_key
t = Twitter(
    auth=OAuth('', '',
               '', ''))

#get user status
print(t.statuses.user_timeline(screen_name="AndrewKLeech"))
