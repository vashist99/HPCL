from django import forms
from django.forms.formsets import BaseFormSet
from django.forms.models import BaseInlineFormSet
from.import models

class DateInput(forms.DateInput):
    input_type = 'date'


class reciept(forms.ModelForm):
    class Meta:
        model=models.reciept
        fields={'locode','pono','inno','pdate','rdate','num'}
        widgets = {
            'pdate': DateInput(attrs={'type': 'date'})
            ,'rdate': DateInput(attrs={'type': 'date'})}


class HR(forms.ModelForm):
    class Meta:
        model=models.child
        fields={'item_des','item_code','quantity','unit','visibility','cost','rec_no'}
    
