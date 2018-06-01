from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import items
from hpemployee.models import hpemployee
from .forms import name


@login_required(login_url="/employee/login/")
def home(request):
    if 'key1' in request.session:
        use=request.session['key1']
        q1=hpemployee.objects.filter(employee_number=use)
        if request.method=='POST':
            des=request.POST['item_name']
            var=name(request.POST)
            if 'logout' in request.POST:
                logout(request)
                return redirect('/employee/login/')
            elif 'see' in request.POST:
                if 'key' in request.session:
                    locate=request.session['key']
                    query=items.objects.filter(item_des=des).filter(locode=locate)
                    return render(request,'inventory/invent.html',{'data':q1,'form':var,'forms':query})
            elif 'see_all' in request.POST:
                all=items.objects.all()
                return render(request,'inventory/invent.html',{'data':q1,'form':var,'ha':all})
        else:
            var=name()

        return render(request,'inventory/invent.html',{'data':q1,'form':var})





# Create your views here.
