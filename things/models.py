from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Model, CharField


# Create your models here.
class Thing(Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=120, unique=False, blank=True)

    def validate_range(self, value):
        if value < 0 or value > 100:
            raise ValidationError(
                message=f'{value} is not between 0 and 100 (inclusive)',
                params={"value": value},
            )
    quantity = models.IntegerField(unique=False, validators=[validate_range])