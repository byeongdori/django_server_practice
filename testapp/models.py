from pyexpat import model
from django.db import models

# Create your models here.

class testapp(models.Model):

    """ Test Model """
    name = models.CharField(max_length=10)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class testApiModel(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
        