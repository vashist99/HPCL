from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from.import models
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class empdetails(UserCreationForm):

    class Meta:
        model=models.hpemployee
        fields=['employee_name','employee_number','DOB','location_code','Email_id','Phone_Number']
        widgets = {
            'DOB': DateInput(attrs={'type': 'date'})}


class query(forms.Form):
    emp_no=forms.IntegerField()

class custom_log(AuthenticationForm):
    username=forms.CharField(label='Employee_number',max_length=30,widget=forms.NumberInput())
