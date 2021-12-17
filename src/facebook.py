from pyfacebook import GraphAPI


class FacebookPy:
    ''' def __init__(self, title, category, subtitle):
        self.title = title
        self.subtitle = subtitle
        self.category = category
        # self.message = self.category.upper() + ' - ' + self.title
        self.message = 'Testando publicação na página do Facebook da Geek News' '''

    def post(self):
        token = 'EAADtLyUoHHMBACuEd0QrMSjMccckzpNIqTQ2idACsaEIVaEPTYQdQon'
        '2NZCEBZCuwcRDqW1XSZB9n4ZCTRnaTyBOuZBAf9NdHF25BafGs'
        'A50h9eGJ1ZAlJjHbbdEEmN38ycCxzRi1mRL2ZAilxAcipCQl'
        'AZBap3BbCudyZBpO8CePpMz0HqoSdimGL'
        'jfZBaECCSEZBzx3qZA6d3ZBsgZDZD'

        api = GraphAPI(access_token=token)

        api.put_object(parent_object='me',
                       connection_name='feed',
                       message="self.message")

        # api.put_photo(
        #     image=open('teste.png', 'rb'),
        #     message='Testando publicação'
        # )

        return
