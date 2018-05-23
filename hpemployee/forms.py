from django import forms



class empdetails(forms.Form):
    name= forms.CharField(label='Employee Name',max_length=100)
    num=forms.IntegerField(label="Employee Number")
    date=forms.DateTimeField(label="date of birth")
