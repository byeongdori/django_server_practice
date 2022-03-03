from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.testapp)
class TestappAdmin(admin.ModelAdmin):

    """ Test App Definition """
    