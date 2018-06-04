from django.db import models
from django.core.validators import ValidationError

class items(models.Model):
    item_code=models.CharField(max_length=100)
    item_des=models.CharField(max_length=100)
    activity=models.CharField(max_length=100)
    quantity=models.IntegerField()
    locode=models.IntegerField()
    unit=models.CharField(max_length=100,blank=True)
    visibility=models.CharField(max_length=100,blank=True)
    cost=models.IntegerField(null=True)
    pono=models.IntegerField(null=True)
    inno=models.IntegerField(null=True)
    pdate=models.DateField(null=True)
    rdate=models.DateField(null=True)




    def __str__(self):
        return self.item_des
