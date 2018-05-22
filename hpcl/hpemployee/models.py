from django.db import models
from datetime import datetime

# Create your models here.
class hpemployee(models.Model):
    employee_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    employee_number=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    DOB=models.DateField()
    preserve_default=False





    def __str__(self):
        return self.employee_name
