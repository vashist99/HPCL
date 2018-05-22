from django.shortcuts import render
from django.http import HttpResponse
from .models import hpemployee
from .forms import empdetails


def employeepage(request):
    var = hpemployee.objects.all().order_by("employee_name") #this was to implement models
    if request.method=='POST':
        form=empdetails(request.POST)
        if form.is_valid():
            return HttpResponse('/Thanks!/')
    else:
        form=empdetails()

    return render(request,'hpemployee\homepage.html',{"form":form})

def employeedetails(request):
    return render(request,"hpemployee\employeedetails.html")
# Create your views here.
