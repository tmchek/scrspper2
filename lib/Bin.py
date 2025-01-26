from requests import Session


class BinResponse:
    'Envía una solicitud a la API BIN::'
    @classmethod
    def __init__(
        self,  
        bin = None,
        ):

        self.bin = bin
        self.session = Session()
        self.url = 'https://bins.antipublic.cc/bins/{}'.format(self.bin)
        self.client = self.session.get(
            url=self.url
            )
        
        self.response = self.client.json()

    @classmethod
    def result(self):
        "Returns a list "
        return (
            self.response['bin'],
            self.response['country_name'],
            self.response['country_flag'],
            self.response['brand'],
            self.response['level'],
            self.response['type'],
            self.response['bank']
            )