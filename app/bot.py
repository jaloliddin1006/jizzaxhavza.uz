from aiogram import Bot, Dispatcher, types
import asyncio


TOKEN = '6057515232:AAEU34QT-caJycclQgn_f17auaAL7QWFWy0'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def send_message_to_bot(chat_id, text):
    await bot.send_message(chat_id, text)

async def main():
    # dp.run_until_disconnected()
    with open('app/data.txt', 'r') as file:
        data = str(file.read().strip())
  
    chat_id = 5804540186  # O'zingizning chat ID raqamingizni qo'ying
   
    await send_message_to_bot(chat_id, data)
    await bot.close()

def run_bot():
    # main()    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

# if __name__ == '__main__':
#     main()    
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())


# print("============================ ok ko ko k ok ok o ko ko ko k ===========================")
