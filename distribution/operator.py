from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from distribution.services import my_job


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')

    @scheduler.scheduled_job('interval', minutes=5, name='auto_job')
    def auto_job():
        my_job()

    scheduler.start()
    print('Scheduler started')
