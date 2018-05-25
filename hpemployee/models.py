from django.db import models
from datetime import date
from django.core.validators import ValidationError

# Create your models here.
class hpemployee(models.Model):
    employee_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    employee_number=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    DOB=models.DateField()
    Email_id=models.EmailField(max_length=100)
    Phone_Number=models.IntegerField()
    preserve_default=False


    def clean(self):

        var =str(self.employee_number)
        var1=str(self.Phone_Number)

        if date.today() <= self.DOB:
            raise ValidationError('Enter a valid date!')
        if len(var)!=8 and var[0]!='3' or var[7]!='0':
            raise ValidationError('enter a valid emloyee number!')

        if len(var1)!=10 and var1[0]!='9' and var1[0]!='8' and var1[0]!='7' and var1[0]!='6':
            raise ValidationError('enter a valid phone number!')


    def __str__(self):
        return self.employee_name
