import os
import time

import pyrogram
from pyrogram import Filters,Client
from pyrogram.api import functions

from pyrobot import COMMAND_HAND_LER

sleeptime = 1

@Client.on_message(Filters.command(["pname"],COMMAND_HAND_LER) & pyrogram.Filters.me)
async def set_name(client, message):
      if sleeptime < time.time():
         await client.send(functions.account.UpdateProfile(first_name=' '.join(message.command[1:])))
         await message.edit('`Name changed succesfully`')
         time.sleep(3)
         await message.delete()
         
@Client.on_message(Filters.command(['pbio'], COMMAND_HAND_LER) & Filters.me)
async def set_bio(client, message):
      if sleeptime < time.time():
         bio = ' '.join(message.command[1:])
         if len(bio) > 70:
            await  message.edit('`Bio too long maximum 70 characters`')
            time.sleep(3)
            await message.delete()
         else:
            await  client.send(functions.account.UpdateProfile(about=bio))
            await  message.edit('`Bio succesfully changed`'.format(bio))
            time.sleep(3)
            await message.delete()

@Client.on_message(Filters.command(['ppic'], COMMAND_HAND_LER) & Filters.me)
async def set_profile_pic(client, message):
      if sleeptime < time.time():
         if message.reply_to_message:
            pic = await message.reply_to_message.download()
         else:
            pic = await message.download()
         await client.set_profile_photo(pic)
         await message.edit('`profile picture set succesfully`')
         os.remove(pic)
         await message.delete()
         
@Client.on_message(Filters.me & Filters.command(['lname']), COMMAND_HAND_LER)
async def onecharacter(client, message):
    if sleeptime < time.time():
       await client.send(functions.account.UpdateProfile(last_name=' '.join(message.command[1:])))
       await  message.edit('`Last name set succesfully`')
       time.sleep(3)
       await message.delete()
