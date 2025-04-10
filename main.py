from os import              ( system )
from src.Client import      ( TelegramConfig )

from heads.Banner import    ( banner, creador )

session_name    = 'rex'
regex           = r'\d{14,16}\|\d{1,2}\|\d{2,4}\|\d{3,4}'
phone_number    = '+18298501406'
api_id          = 20230546
api_hash        = '687aa22188883fd3d995a41c928454fe'
bot_token       = '7934220197:AAEeyF0O5OKBfSG_ch-qmnYyzVaQ7huztmE'

chat_id_free    = -1002456099586
chat_id_premium = -1002267171264



if __name__ == "__main__":
    system('clear || cls')
    banner()
    creador()   
    TelegramConfig(
        session_name,
        regex,
        phone_number,
        api_id,
        api_hash,
        bot_token,        
        chat_id_free,
        chat_id_premium
        )
