from twitterapi import Twitter
from facebookapi import Facebook
from instagramapi import Instagram

class MessageSender:
    def __init__(self):
        pass

    def instagramSendMessage(self, message="", image=""):
        instagram = Instagram()
        instagram.SendMessage(message, image)

    def facebookSendMessage(self, message="", image=""):
        facebook = Facebook()
        facebook.SendMessage(message, image)

    def twitterSendMessage(self, message="", image=""):
        twitter = Twitter()
        twitter.SendMessage(message, image)