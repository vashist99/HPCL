from django import forms
from django.forms.formsets import BaseFormSet
from django.forms.models import BaseInlineFormSet
from.import models

ch=models.
ITEMS=[tuple([x,ch.item_des]) for x in range(6)]
class DateInput(forms.DateInput):
    input_type = 'date'


class rec(forms.ModelForm):
    class Meta:
        model=models.reciept
        fields={'locode','pono','inno','pdate','rdate','num'}
        widgets = {
            'pdate': DateInput(attrs={'type': 'date'})
            ,'rdate': DateInput(attrs={'type': 'date'})}


class HR(forms.ModelForm):
    class Meta:
        model=models.child
        fields={'item_des','quantity','cost'}
        widget=forms.Select(choices=ITEMS)

class itemmaster(forms.ModelForm):
    class Meta:
        model=models.child
        fields={'item_des','item_code','unit','visibility'}
