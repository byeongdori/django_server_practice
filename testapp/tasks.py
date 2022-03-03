from __future__ import absolute_import, unicode_literals

from celery import Celery
from celery.schedules import crontab
from . import models as testapp_models

app = Celery("config")
app.config_from_object('django.conf:settings', namespace='CELERY')

@app.task
def test_celery_func(name, text, price):
    testapp_models.testapp.objects.create(name=name, description=text, price=price)
    return 1

@app.task
def test_api_celery_func(text):
    pass

@app.task
def test_celery_add_func(x, y):
    return x + y

@app.task
def test_celery_execute():
    print("Executed!")
    return "Executed"