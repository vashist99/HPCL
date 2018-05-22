from django.shortcuts import render
from django.http import HttpResponse
from .models import hpemployee
from .forms import empdetails,query


def employeepage(request):
    #var = hpemployee.objects.all().order_by("employee_name") #this was to implement models
    if request.method=='POST':
        form=empdetails(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks!')
    else:
        form=empdetails()

    return render(request,'hpemployee\homepage.html',{"form":form})

def employeedetails(request):

    if request.method=='POST':
        num=query(request.POST)

        if num.is_valid():
            #return HttpResponse('hello')

            var3=hpemployee.objects.all().order_by("employee_number")
            return render(request,"hpemployee\employeedetails.html",{"form":num,"forms":var3})

    else:
        num=query()

    return render(request,"hpemployee\employeedetails.html",{"form":num})
# Create your views here.
