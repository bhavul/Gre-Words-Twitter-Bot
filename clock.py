from apscheduler.schedulers.blocking import BlockingScheduler
from AwesomeGreBot import tweetANewWord

sched = BlockingScheduler()

sched.add_job(tweetANewWord, 'cron', hour='9-22', minute='10,30,50')

sched.start()
