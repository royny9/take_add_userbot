from pyrogram import Client
import data


TARGET = int(open(r'E:\my brain\take_add_userbot\chat_id.txt').readline())
print(TARGET)
app = Client('mym_ss', api_hash=data.api_hash, api_id=data.api_id)

async def main():
    async with app:
        with open(r'ids_us.txt', 'w+') as fi:
            async for member in app.get_chat_members(TARGET,limit=0):
                fi.write(str(member.user.id))
                fi.write('\n')
            fi.close()

            
app.run(main())
