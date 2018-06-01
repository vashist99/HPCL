from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import hpemployee
from .forms import empdetails,query,custom_log
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

def employeepage(request):
    #var = hpemployee.objects.all().order_by("employee_name") #this was to implement models
    if request.method=='POST':
        form=empdetails(request.POST)
        var=request.POST['employee_number']
        var1=int(var)
        var2=request.POST['Email_id']
        var3=request.POST['password1']


        if form.is_valid():
            num=hpemployee.objects.filter(employee_number=var1)
            if not num:
                use=form.save() #user is returned
                user=User.objects.create_superuser(username=var,password=str(var3),email=str(var2))


            else:
                a=request.POST['employee_name']
                b=request.POST['DOB']
                c=request.POST['location_code']

                hpemployee.objects.filter(employee_number=var1).update(employee_name=a,DOB=b,location_code=c)
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
                return render(request,"hpemployee\employeedetails.html",{"form1":num,"forms":num2})

            elif 'delete' in request.POST:
                num2.delete()
                return HttpResponse('the details of have been deleted from the database')

            elif 'update' in request.POST:
                form=empdetails()
                return render(request,"hpemployee\homepage.html",{"form":form})


        else:
            return HttpResponse('invalid entry!')

    else:
        num=query()

    return render(request,"hpemployee\employeedetails.html",{"form1":num})

def log(request):
    if request.method=='POST':
        form=custom_log(data=request.POST)
        var=request.POST['username']
        if form.is_valid():
            user=form.get_user()
            query=hpemployee.objects.get(employee_number=var)
            login(request,user)
            request.session['key']=query.location_code
            request.session['key1']=query.employee_number
            return redirect('/inventory/')


    else:
        form=custom_log()

    return render(request,'hpemployee\login.html',{'form':form})
