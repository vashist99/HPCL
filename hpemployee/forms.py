from django import forms
from.import models

class DateInput(forms.DateInput):
    input_type = 'date'

class empdetails(forms.ModelForm):
    class Meta:
        model=models.hpemployee
        fields=['employee_name','employee_number','DOB','location','Email_id','Phone_Number']
        widgets = {
            'DOB': DateInput(attrs={'type': 'date'})}

class query(forms.Form):
    emp_no=forms.IntegerField()
