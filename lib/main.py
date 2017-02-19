from celery import Celery
from crawler import generator_files
from datetime import timedelta

app = Celery('main', broker='pyamqp://lisa:123456789@rabbit//')
app.config_from_object(__name__)

@app.task
def run():
    generator_files()

CELERYBEAT_SCHEDULE = {
    'every-8-hours': {
        'task': 'main.run',
        'schedule': timedelta(hours=8),
    },
}