from lib.Bin import         ( BinResponse )
from lib.Bot import         ( SendPostMessage )
from lib.Card import        ( FindsCard )
from lib.Extra import       ( ExtraPoleador )
from func.keywords import   ( keywords )
from dataclasses import     ( dataclass )

from re import              (  sub )
from colorama import        ( Fore)
from telethon.sync import   ( TelegramClient, events)
from func.plantillas import ( Plantilla_free, Plantilla_Premium )



cards_list:set = set()

@dataclass
class TelegramConfig:
    'Sesion de telegram::'
    @classmethod
    def __init__(
        self,
        name=None,
        regex=None,
        phone_number=None,
        api_id=None,
        api_hash=None,
        bot_token=None,
        photo_free=None,
        chat_id_free=None,
        photo_premium=None,
        chat_id_premium=None,
        ):
        
        

        self.session_name    = name
        self.regex           = regex
        self.phone_number    = phone_number
        self.api_id          = api_id
        self.api_hash        = api_hash
        self.bot_token       = bot_token
        self.photo_free      = photo_free
        self.chat_id_free    = chat_id_free
        self.photo_premium   = photo_premium
        self.chat_id_premium = chat_id_premium


        self.client = TelegramClient(
            self.session_name,
            self.api_id,
            self.api_hash,    
        )

        self.client.start(self.phone_number)

        @self.client.on(
            events.MessageEdited()
            )
        async def onMessageEdited(message):
            try:
                "Iniciativa de codigo para el parse de message y texto"
                getMsg      = message.message.message.upper()
                regeh       = sub(self.regex, r'<code>\g<0></code>', getMsg)
                cards       = FindsCard().finds_cards(regeh)
                ccs         = '{}|{}|{}|{}'.format(cards[0],cards[1],cards[2],cards[3])

                if ccs in cards_list: return

                bin_chk     = BinResponse(cards[0][:6]).result()
                ExtraPole   = f'{cards[0][:12]}xxxx|{cards[1]}|{cards[2]}|rnd'


                texto_free  = Plantilla_free.format(
                                    cards[0],   cards[1],
                                    cards[2],   cards[3],
                                    ExtraPole, 
                                    bin_chk[0], bin_chk[1],
                                    bin_chk[2], bin_chk[3],
                                    bin_chk[4], bin_chk[5],
                                    bin_chk[6]  )
            
                SendPostMessage(
                        text    = str(texto_free),
                        token   = str(self.bot_token),
                        chat_id = int(self.chat_id_free),
                        photo   = self.photo_free
                        )
                    
                cards_list.add(ccs)

                for live in keywords:
                    if live in getMsg:
                        
                        texto_premium = Plantilla_Premium.format(cards[0],
                                                                 cards[1],
                                                                 cards[2], 
                                                                 cards[3],
                                                                 live, 
                                                                 ExtraPole,
                                                                 bin_chk[0], 
                                                                 bin_chk[1], 
                                                                 bin_chk[2], 
                                                                 bin_chk[3],
                                                                 bin_chk[4],
                                                                 bin_chk[5],
                                                                 bin_chk[6]
                                                                 )
                        SendPostMessage(
                            text    = str(texto_premium),
                            token   = str(self.bot_token),
                            chat_id = int(self.chat_id_premium),
                            photo   = self.photo_premium,
                            )
                        
                        print( Fore.GREEN + f'\n[⌁] - Aprovada ✅: {live}')
                        return ...
                return ' [⌁] scrappings...👾'
            except:
                pass
            
        self.client.run_until_disconnected()


