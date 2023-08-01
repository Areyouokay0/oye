import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5951942864:AAFVVBT3ZwmNwek6W6F_xQ-v3sX2DSymTcw")

API_ID = int(os.environ.get("API_ID", "8206404"))

API_HASH = os.environ.get("API_HASH", "e935d9b56e3fd2c05c743093efb761c9")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
