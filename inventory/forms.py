from django import forms
from django.forms.formsets import BaseFormSet
from.import models

class DateInput(forms.DateInput):
    input_type = 'date'


class name(forms.Form):
    item_name=forms.CharField(max_length=100)




class HR(forms.ModelForm):
    class Meta:
        model=models.items
        fields={'item_des','item_code','activity','quantity','unit','visibility','cost','pono','pdate','inno','rdate'}


        widgets = {
            'pdate': DateInput(attrs={'type': 'date'})
            ,'rdate': DateInput(attrs={'type': 'date'})}
