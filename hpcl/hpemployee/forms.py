<<<<<<< HEAD
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

class query(forms.ModelForm):
    class Meta:
        model=models.hpemployee
        fields=['employee_number']
||||||| merged common ancestors
=======
from django import forms
from.import models



class empdetails(forms.ModelForm):
    class Meta:
        model=models.hpemployee
        fields=['employee_name','employee_number','DOB','location']

class query(forms.Form):
    num=forms.IntegerField()
>>>>>>> 3a45434f507b04cda85f2f44002807efe1a5b88c
