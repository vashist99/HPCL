from django import forms
from django.forms.formsets import BaseFormSet
from django.forms.models import BaseInlineFormSet
from.import models
def get_choices():
    LIST=[]
    ch=models.child()
    while ch:
        LIST.append(ch)

    return LIST

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
    def __init__(self,*args,**kwargs):
        super(HR,self).__init__(*args,**kwargs)
        self.fields['item_des']=forms.ModelChoiceField(
         choices=get_choices()
        )
    class Meta:
        model=models.child
        fields={'item_des','quantity','cost'}

class itemmaster(forms.ModelForm):
    class Meta:
        model=models.child
        fields={'item_des','item_code','unit','visibility'}
