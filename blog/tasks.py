from celery import shared_task
import time
from datetime import datetime,timedelta

@shared_task
def test_task(name):

    print(f'Welcome to my site {name}')
    time.sleep(5)
    return f'Task finished for Mr/Ms {name}'

@shared_task
def say_hello(name):
    print(f'Hello {name}')

eta_time = datetime.utcnow() + timedelta(seconds=30)
say_hello.apply_async(('arshia',),eta=eta_time)