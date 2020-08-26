from instabot import Bot
import os

class Instagram:
    def __init__(self):
        self.bot = Bot()
        self.bot.login(username="XXXX", password="XXXX",is_threaded=True)

    def SendMessage(self, message="", image=""):
        self.bot.upload_photo(photo=image, caption=message)
        oldImage = image + ".REMOVE_ME"
        newImage = image
        os.rename(oldImage, newImage)