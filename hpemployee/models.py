from django.db import models

# Create your models here.
class hpemployee(models.Model):
    employee_name=models.CharField(max_length=100)
    location=models.TextField()

    def __str__(self):
        return self.employee_name
        
