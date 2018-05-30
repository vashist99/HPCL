from django import forms

class name(forms.Form):
    item_name=forms.CharFields(max_length=100)
