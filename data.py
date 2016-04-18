from twitter import *

#Put in token, token_key, con_secret, con_secret_key
t = Twitter(
    auth=OAuth('705153959368007680-F5OUf8pvmOlXku1b7gpJPSAToqzV4Fb', 'bEGLkUJBziLc17EuKLTAMio8ChmFxP9aHYADwRXnxDsoC',
               'gYDgR8lcTGcVZS9ucuEIYsMuj', '1dwHsLDN2go3aleQ8Q2vcKRfLETc51ipsP8310ayizL2p3Ycii'))

#get user status
print(t.statuses.user_timeline(screen_name="AndrewKLeech"))
