from django import forms
from django.forms.formsets import BaseFormSet
from django.forms.models import BaseInlineFormSet
from.import models

class DateInput(forms.DateInput):
    input_type = 'date'


class name(forms.Form):
    item_name=forms.CharField(max_length=100)


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
        fields={'item_des','item_code','activity','quantity','unit','visibility','cost','rec_no'}
        exclude=('field_id',)
