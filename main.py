#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 6134343, #get it from https://my.telegram.org/auth
    api_hash="344493a60221b6483e47b00ff1461708", #get it from https://my.telegram.org/auth
    bot_token="5929089968:AAFVBq4UvQfYTKyvpfTWSByIVG_P92Ahd8s", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
