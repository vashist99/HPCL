from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from.import models


class DateInput(forms.DateInput):
    input_type = 'date'

class empdetails(UserCreationForm,forms.ModelForm):

    class Meta:
        model=models.hpemployee
        fields=['employee_name','employee_number','DOB','location_code','location','Email_id','Phone_Number']
        widgets = {
            'DOB': DateInput(attrs={'type': 'date'})}


class query(forms.Form):
    emp_no=forms.IntegerField()

class custom_log(AuthenticationForm):
    username=forms.IntegerField(label='Employee_number')
    password=forms.CharField(label="Password",max_length=30,widget=forms.PasswordInput())
