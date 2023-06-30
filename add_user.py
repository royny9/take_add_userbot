from pyrogram import Client
import data
import time

def normal_open():
    data_set_users = open(r'E:\my brain\take_add_userbot\ids_us.txt').readlines()
    ss = []
    for i in range(len(data_set_users)):
        s = data_set_users[i]
        ss += [int(s[:-1])]
    return ss

data_users = normal_open()
new_chat_id = -846221749

app = Client('adds_user', api_hash=data.api_hash, api_id=data.api_id)


async def add_us(new_chat_id, data_users):
    await app.add_chat_members(new_chat_id, data_users, forward_limit=10000)
    
    
app.run(add_us(new_chat_id,data_users))
