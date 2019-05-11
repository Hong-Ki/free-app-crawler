from apscheduler.schedulers.blocking import BlockingScheduler
from crawler import getAppInfo, getPlatforms
import os
import telegram
dir(telegram)

print('INIT')
bot_token = os.getenv('BOT_TOKEN')
sched = BlockingScheduler()
bot = telegram.Bot(token=bot_token)

current = []


def sendMessage():
    message = ''
    platforms = getPlatforms()

    print(platforms)
    for platform in platforms:
        if len(platform['time']) > 9:
            continue
        message = platform['title']+'\n'+platform['link']+'\n\n'
        apps = getAppInfo(platform['link'])
        print(apps)
        for i in range(apps['length']):
            if apps['titles']:
                message += '-'+apps['titles'][i] + '\n'
            message += apps['links'][i] + '\n'
        result = bot.sendMessage(chat_id='-1001166284442', text=message)
        current.append(platform['title'])


@sched.scheduled_job('interval', minutes=25)
def timed_job():
    print('CHECK')
    if (len(current) < 2):
        sendMessage()


@sched.scheduled_job('cron', hour=8)
def scheduled_job():
    current.clear()
    print('SEND_MESSAGE')
    sendMessage()


sched.start()
