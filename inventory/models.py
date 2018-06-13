from django.db import models
from django.core.validators import ValidationError


class reciept(models.Model):
    locode=models.IntegerField(null=True)
    pono=models.IntegerField(null=True)
    inno=models.IntegerField(null=True)
    pdate=models.DateField(null=True)
    rdate=models.DateField(null=True)
    num=models.IntegerField(null=True)

    def __str__(self):
        return self.num

class child(models.Model):
    rec_no=models.IntegerField(null=True,blank=True)
    item_des=models.CharField(max_length=50,null=True,blank=True)
    item_code=models.CharField(max_length=50,null=True,blank=True)
    activity=models.CharField(max_length=50,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    cost=models.IntegerField(null=True,blank=True)
    unit=models.CharField(max_length=50,blank=True)
    visibility=models.CharField(max_length=50,blank=True)
    loc=models.IntegerField(null=True,blank=True)

    def clean(self):
        if self.visibility!='yes' or self.visibility!='no':
            raise ValidationError('enter a valid visibility')



    def __str__(self):
        return self.item_des
