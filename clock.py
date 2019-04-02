from apscheduler.schedulers.blocking import BlockingScheduler
from AwesomeGreBot import tweetANewWord

sched = BlockingScheduler()

sched.add_job(tweetANewWord, 'cron', hour='1-23', minute='0,10,20,30,40,50')

print "Starting scheuler!"
sched.start()
