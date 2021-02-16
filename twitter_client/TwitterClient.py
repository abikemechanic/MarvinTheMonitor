import tweepy

from twitter_secrets import TwitterSecrets


class TwitterClient:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(TwitterSecrets.api_key, TwitterSecrets.api_key_secret)
        self.auth.set_access_token(TwitterSecrets.access_token, TwitterSecrets.access_token_secret)

        self.api = tweepy.API(self.auth)

    def update_status_with_media(self, status_text, status_media_file):
        resp = self.api.media_upload(status_media_file)

    def update_staus_with_test(self, status_text):
        self.api.update_status(status_text)


tc = TwitterClient()
