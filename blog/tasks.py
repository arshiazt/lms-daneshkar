from celery import shared_task
import time

@shared_task
def test_task(name):

    print(f'Welcome to my site {name}')
    time.sleep(5)
    return f'Task finished for Mr/Ms {name}'