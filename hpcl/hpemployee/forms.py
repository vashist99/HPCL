from django import forms
from.import models



class empdetails(forms.ModelForm):
    class Meta:
        model=models.hpemployee
        fields=['employee_name','employee_number','DOB','location']

class query(forms.Form):
    num=forms.IntegerField()
