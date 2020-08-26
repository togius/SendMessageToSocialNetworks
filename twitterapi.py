import tweepy


class Twitter:
    def __init__(self):
        twitter_auth_keys = {
            "consumer_key": "XXXXXXXXXXXXXXXX",
            "consumer_secret": "XXXXXXXXXXXXXXXX",
            "access_token": "XXXX-XXXX",
            "access_token_secret": "XXXX"
        }
        auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
        )
        auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
        )
        self.api = tweepy.API(auth)

    def SendMessage(self, message="", image=""):
        media = None
        tweet = ""
        if image != "":
            media = self.api.media_upload(image)
        if message != "":
            tweet = message
        if media != None:
            post_result = self.api.update_status(status=tweet, media_ids=[media.media_id])
        else:
            post_result = self.api.update_status(status=tweet)

        print("Gonderilen tweet: " + message)
