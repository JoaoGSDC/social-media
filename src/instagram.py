from instabot import Bot
import os
import shutil
from src.photoshop import PhotoshopPy


class InstagramPy:
    ''' def __init__(self, title, category, subtitle):
        self.title = title
        self.subtitle = subtitle
        self.category = category
        # self.message = self.category.upper() + ' - ' + self.title
        self.message = 'Testando publicação na página do Instagram da Geek News' '''

    def clean_up(i):
        dir = "config"
        remove_me = "imgs\{}.REMOVE_ME".format(i)
        # checking whether config folder exists or not
        if os.path.exists(dir):
            try:
                # removing it so we can upload new image
                shutil.rmtree(dir)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))
        if os.path.exists(remove_me):
            src = os.path.realpath("imgs\{}".format(i))
            os.rename(remove_me, src)

    def post(self):
        self.clean_up()

        os.system('rm -rf config')
        bot = Bot()
        bot.login(username='portal.geeknews', password='@Senha135')
        bot.logout(username='portal.geeknews')

        # photoshopy = PhotoshopPy()
        # photoshopy.openApp()

        bot.upload_photo(r"C:\Users\JoaoGSDC\Documents\Dev\Pessoal\social-media\img\instagram_feed.png",
                         caption="Testando postagem no insta!")
        bot.logout()


#        self.clean_up()
#
#        import pythoncom
#        pythoncom.CoInitialize()
#
#        photoshopy = PhotoshopPy()
#        photoshopy.openApp()
#
#        bot = Bot()
#        bot.login(username='portal.geeknews', password='@Senha135')
#
#        bot.upload_photo(r"C:\Users\JoaoGSDC\Documents\Dev\Pessoal\social-media\tests\resources\instagram_feed.png",
#                         caption="self.message")
#
#        return

    def auth(self):
        import pythoncom
        pythoncom.CoInitialize()

        bot = Bot()
        bot.login(username='portal.geeknews', password='@Senha135')
        return
