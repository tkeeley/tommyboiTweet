# Make sure you create a new file and paste your API keys from apps.twitter.com into variables. Save the file as auth.py

# Run this everyday by setting up a cronjob for it
# env EDITOR=nano crontab -e
# 0 12 * * *  /full/path/to/python /full/path/to/script.py

from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = "Hello @GovernorTomWolf This is your daily reminder that you're an idiot and no one likes you!"
twitter.update_status(status=message)
print("Tweeted: " + message)