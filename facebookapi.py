import facebook

class Facebook:
    def __init__(self):
        access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        self.graph = facebook.GraphAPI(access_token)

    def SendMessage(self, message="", image=""):
        if image == "":
            self.graph.put_object(parent_object="me",
                                  connection_name="feed",
                                  message=message)
        else:
            self.graph.put_photo(image=open(image, 'rb'),
                            message=message)


