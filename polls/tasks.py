from celery import shared_task

@shared_task(queue='high_priority')
def my_high_priority_task():
    # ... your task logic ...

@shared_task  # This will go to the 'default' queue
def my_default_task():
    # ... your task logic ...
