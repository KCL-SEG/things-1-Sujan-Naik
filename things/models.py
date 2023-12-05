from django.db import models
from django.db.models import Model, CharField


# Create your models here.
class Thing(Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    quantity = models.IntegerField()