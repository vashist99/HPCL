from django.shortcuts import render
from django.http import HttpResponse
from .models import hpemployee
from .forms import empdetails,query



def employeepage(request):
    #var = hpemployee.objects.all().order_by("employee_name") #this was to implement models
    if request.method=='POST':
        form=empdetails(request.POST)
        var=request.POST['employee_number']
        var1=int(var)


        if form.is_valid():
            num=hpemployee.objects.filter(employee_number=var1)
            if not num:
                form.save()
            else:
                a=request.POST['employee_name']
                b=request.POST['DOB']
                c=request.POST['location']
                hpemployee.objects.filter(employee_number=var1).update(employee_name=a,DOB=b,location=c)
            #return HttpResponse('Thanks!')
    else:
        form=empdetails()

    return render(request,'hpemployee\homepage.html',{"form":form})

def employeedetails(request):

    if request.method=='POST':

        num=query(request.POST)
        var=request.POST['emp_no']
        var1=int(var)

        if num.is_valid():
            num2=hpemployee.objects.filter(employee_number=var1)
            if 'getdetails' in request.POST:
                return render(request,"hpemployee\employeedetails.html",{"form":num,"forms":num2})

            elif 'delete' in request.POST:
                num2.delete()
                return HttpResponse('the details of have been deleted from the database')

            elif 'update' in request.POST:
                return render(request,"hpemployee\homepage.html",{"form":num})


        else:
            return HttpResponse('invalid entry!')

    else:
        num=query()

    return render(request,"hpemployee\employeedetails.html",{"form":num})
