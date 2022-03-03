from __future__ import absolute_import, unicode_literals

from celery import Celery
from celery.schedules import crontab
from . import models as testapp_models

app = Celery("config")
app.config_from_object('django.conf:settings', namespace='CELERY')

@app.task
def test_celery_func(name, text, price):
    testapp_models.testapp.objects.create(name=name, description=text, price=price)
    return print("testapp model created!")
