import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'test_adding': {
        'task': 'apps.sites.tasks.refresh_site_statuses',
        'schedule': 60.0,
    }
}

