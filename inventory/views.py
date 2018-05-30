from django.shortcuts import render,redirect
from django.contrib.auth.decoratora import login_required
from django.http import HttpResponse
from .models import item
from .forms import name


@login_required(login_url="/employee/login/")
def items(request):

    if request.method=='POST':
        des=request.POST['item_des']
        var=name(request.POST)

        if logout in request.POST:
            logout(request)
            return redirect('/employee/login/')
        elif see in request.POST:
            query=items.objects.filter(item_des=var,locode=request.session['0'])
            return render(request,'inventory/invent.html',{'form':var,'forms':query})
        elif see_all in request.POST:
            all=items()
            return render(request,'inventory/invent.html',{'form':var,'key':all})
    else:
        var=name()
    return render(request,'inventory/invent.html',{'form':var})            



# Create your views here.
