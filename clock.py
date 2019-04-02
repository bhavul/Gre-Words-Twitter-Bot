from apscheduler.schedulers.blocking import BlockingScheduler
from AwesomeGreBot import tweetANewWord

sched = BlockingScheduler()

sched.add_job(tweetANewWord, 'cron', hour='1-23', minute='10,25,30,50,55')

sched.start()
