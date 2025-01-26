from requests import Session


class SendPostMessage():
    'Envía un mensaje a un chat telegram::'
    @classmethod
    def __init__(
        self,  
        token: str       = None,
        chat_id: int     = None, 
        text: str        = None,
        photo            = None
        ):
       
        self.photo  = photo
        self.client = Session()
        self.text   = str(text)
        self.token  = str(token)
        self.id     = int(chat_id)

        self.url    = "https://api.telegram.org/bot{}/sendPhoto".format(self.token)

        self.parameters = {
            'chat_id': self.id,
            'caption': self.text,
            'photo': self.photo,
            'parse_mode': 'html',
            'reply_markup': {'inline_keyboard': [[{'text': '🇩🇴𝕺𝖓𝖊 𝖙𝖊𝖈𝖍 𝕿𝖊𝖆𝖒 🇩🇴 𝓔𝓁 𝓟𝓪𝓽𝓻ó𝓷', 'url': 'https://t.me/+KaDXI8DMQW80MWYx'}]]}}

        self.response = self.client.post(
            url  = self.url, 
            json = self.parameters)
            

    @classmethod
    def __str__(self) -> str:
        return '{}'.format(
            self.response.json()
            )
