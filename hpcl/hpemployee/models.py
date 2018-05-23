
from django.db import models
from datetime import datetime

# Create your models here.
class hpemployee(models.Model):
    employee_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    employee_number=models.IntegerField(max_length=7)
    date=models.DateTimeField(auto_now_add=True)
    DOB=models.DateField(max_length=100)
    Email_id=models.EmailField(max_length=100,default="gnhegde@hpcl.in")
    Phone_Number=models.IntegerField(default="9920635887")
    preserve_default=False





    def __str__(self):
        return self.employee_name
