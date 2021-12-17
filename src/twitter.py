from tweepy import API
from tweepy import OAuthHandler


class TwitterPy:
    def __init__(self, title, category, subtitle):
        self.title = title
        self.subtitle = subtitle
        self.category = category
        # self.message = self.category.upper() + ' - ' + self.title
        self.message = 'Testando publicação na página do Facebook da Geek News'

    def post(self):
        # Authenticate to Twitter
        auth = OAuthHandler("pGBDoAaEpkliVKBOLwjtcmHGc",
                            "xF3g1wrP50b6BlZEd20u4oVfjgH1FGQcuWUzlQO5aUWOufvlhw")
        auth.set_access_token("622518493-6VcLIPprbQbv9wkcBBPvCle8vsjU9fE85Dq9oStl",
                              "tH9aKQbQQ1iRdYTcLSsPwitl44BkAc6jilrsU0ifnXvZhq")

        api = API(auth)

        try:
            api.verify_credentials()
        except:
            print("Error during authentication")

        api.update_status("Test tweet from Tweepy Python")

        return
