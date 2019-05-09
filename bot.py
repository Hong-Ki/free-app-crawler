from apscheduler.schedulers.blocking import BlockingScheduler
from crawler import getAppInfo, getPlatforms
import os
import telegram
dir(telegram)

bot_token = os.getenv('BOT_TOKEN')
sched = BlockingScheduler()
bot = telegram.Bot(token=bot_token)

current = []


def sendMessage():
    message = ''
    platforms = getPlatforms()

    for platform in platforms:
        if len(platform['time']) > 9:
            continue
        message = platform['title']+'\n'+platform['link']+'\n\n'
        apps = getAppInfo(platform['link'])
        for i in range(apps['length']):
            message += '-' + apps['titles'][i] + '\n' + apps['links'][i] + '\n'
        result = bot.sendMessage(chat_id='-1001166284442', text=message)
        current.append(platform['title'])


@sched.scheduled_job('interval', seconds=5)
# @sched.scheduled_job('interval', minutes=25)
def timed_job():
    if (len(current) < 2):
        sendMessage()


@sched.scheduled_job('cron', hour=8)
def scheduled_job():
    current.clear()
    sendMessage()


sched.start()
