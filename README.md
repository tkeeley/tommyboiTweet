# tommyboiTweet
 Tweets at PA Governor Tom Wolf daily to remind him he's an idiot.

 Make sure you create a new file and paste your API keys from apps.twitter.com into variables. Save the file as auth.py
 Use the following for your variables

    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret

 Run this everyday by setting up a cronjob for it
 env EDITOR=nano crontab -e
 0 12 * * *  /full/path/to/python /full/path/to/script.py
