import os
from os import              ( system )
from lib.Client import      ( TelegramConfig )

from heads.Banner import    ( banner, creador )

session_name    = 'rex'
regex           = r'\d{14,16}\|\d{1,2}\|\d{2,4}\|\d{3,4}'
phone_number    = '+52 5644968614'
api_id          = 24648014
api_hash        = '3575a0f1524c2a08cc297fbd5355e318'
bot_token       = '7028828829:AAH12Vb8mwnY5GXxc-9qF8Ij1qr2huQcFic'
photo_free      = 'https://i.imgur.com/3xMKhXg.jpeg'
chat_id_free    = -1002254488425
photo_premium   = 'https://i.imgur.com/ZND2sko.jpeg'
chat_id_premium = -1002254488425


# Testeo de la clase TelegramConfig
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
        photo_free,
        chat_id_free,
        photo_premium,
        chat_id_premium,
    )
