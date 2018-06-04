from django.db import models
from datetime import date
from django.core.validators import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class hpemployee(AbstractBaseUser):
    employee_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100,blank=True)
    location_code=models.IntegerField()
    location=models.CharField(max_length=100,blank=True,null=True)
    employee_number=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    DOB=models.DateField(max_length=100)
    Email_id=models.EmailField(max_length=100)
    Phone_Number=models.IntegerField()
    status=models.CharField(max_length=100,blank=True)
    last_login=models.CharField(max_length=100,default=" ",blank=True)


    var=UserCreationForm()
    USERNAME_FIELD='employee_number'


    def clean(self):
        var =str(self.employee_number)
        var1=str(self.Phone_Number)
        var3=str(self.location_code)
        if self.DOB>=date.today():
            raise ValidationError('Enter a valid date!')
        if len(var)!=8 and (var[0]!=3 or var[7]!=0):
            raise ValidationError('enter a valid emloyee number!')

        if len(var1)!=10 and var1[0]!=9 and var1[0]!=8 and var1[0]!=7 and var1[0]!=6:
            raise ValidationError('enter a valid phone number!')
        if len(var3)!=5:
            raise ValidationError('Enter a valid location code!')

    def __str__(self):
        return self.employee_name
