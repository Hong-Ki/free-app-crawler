from apscheduler.schedulers.blocking import BlockingScheduler
from crawler import getAppLinks, getPlatforms
import os
import telegram
dir(telegram)

bot_token = os.getenv('BOT_TOKEN')

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=25)
def timed_job():
    updates = bot.getUpdates()


@sched.scheduled_job('cron', hour=8)
def scheduled_job():
    message = ''
    platforms = getPlatforms()

    for platform in platforms:
        if len(platform['time']) > 9:
            continue
        message = platform['title']+'\n'+platform['link']+'\n\n'
        links = getAppLinks(platform['link'])
        for link in links:
            message += link + '\n'
        result = bot.sendMessage(chat_id='-1001166284442', text=message)


sched.start()
