import tweepy

def post_x(content):
    API_KEY = "your_key"
    API_SECRET = "your_secret"
    TOKEN = "your_token"
    SECRET = "your_token_secret"

    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, TOKEN, SECRET)
    api = tweepy.API(auth)

    api.update_status(content["x"])
    print("Posted to X")
