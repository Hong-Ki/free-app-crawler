import telegram
dir(telegram)


my_token = '695803293:AAG5FyA1ptFScX6E1ZGtOL4n2aj7CiuLkZM'
print('init bot')
bot = telegram.Bot(token=my_token)
updates = bot.getUpdates()

result = bot.sendMessage(chat_id='-1001166284442', text="I'm bot")

print(result)
