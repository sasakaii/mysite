import os
from celery import Celery
from django.conf import settings

from kombu import Queue

CELERY_QUEUES = (
    Queue('queue1', routing_key='queue1'),
    Queue('queue2', routing_key='queue2'),
)
   

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # Replace 'your_project_name'

app = Celery('mysite')  # Replace 'your_project_name'

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
