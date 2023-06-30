import aiogram as ai


token = '5842987049:AAFQBvg66at6s7PLTo46L0lT4jlTvrQtrzo'
bot = ai.Bot(token)
disp = ai.Dispatcher(bot)

@disp.message_handler(commands=['start'])
async def return_chat_id(message: ai.types.Message):
    output_chat = message.chat.id
    await message.reply(str(output_chat)) #отправит ID в чат
    with open(r'chat_id.txt', 'w+') as data:
            data.write(str(output_chat))
            data.close()


if __name__ == '__main__':
    ai.executor.start_polling(disp)
