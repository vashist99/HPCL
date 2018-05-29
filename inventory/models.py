from django.db import models
from datetime import date
from django.core.validators import ValidationError

class items(models.Model):
    item_code=models.TextField(max_length=100)
    item_des=models.TextField(max_length=100)
    activity=models.TextField(max_length=100)
    quantity=models.IntegerField()
    locode=models.IntegerField()

# Create your models here.
