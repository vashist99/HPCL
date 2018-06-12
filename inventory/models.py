from django.db import models
from django.core.validators import ValidationError


class reciept(models.Model):
    locode=models.IntegerField(null=True)
    pono=models.IntegerField(null=True)
    inno=models.IntegerField(null=True)
    pdate=models.DateField(null=True)
    rdate=models.DateField(null=True)
    num=models.IntegerField(null=True)

class child(models.Model):
    rec_no=models.IntegerField(null=True)
    item_des=models.CharField(max_length=50)
    item_code=models.CharField(max_length=50)
    activity=models.CharField(max_length=50)
    quantity=models.IntegerField()
    cost=models.IntegerField(null=True)
    unit=models.CharField(max_length=50,blank=True)
    visibility=models.CharField(max_length=50,blank=True)
    loc=models.IntegerField(max_length=50,null=True)

    def __str__(self):
        return self.item_des
