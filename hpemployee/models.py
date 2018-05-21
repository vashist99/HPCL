from django.db import models
from datetime import datetime

# Create your models here.
class hpemployee(models.Model):
    employee_name=models.CharField(max_length=100)
    location=models.TextField()
    employee_number=models.IntegerField(default='30084769')
    date=models.DateTimeField(auto_now_add=True)
    DOB=models.DateTimeField(default=datetime(1963,12,2,15,30,59,354343))
    preserve_default=False

    def __str__(self):
        return self.employee_name
