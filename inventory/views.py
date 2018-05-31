from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import items
from .forms import name

@login_required(login_url='/employee/login/')
def home(request):

    if request.method=='POST':
        #return HttpResponse(request.POST)
        des=request.POST['item_name']
        var=name(request.POST)


        if 'logout' in request.POST:
            logout(request)
            return redirect('/employee/login')
        elif 'see' in request.POST:
            if 'key' in request.session:
                #return HttpResponse(request.session['key'])
                locate=request.session['key']

                query=items.objects.filter(item_des=des).filter(locode=locate)
                return render(request,'inventory/invent.html',{'form':var,'forms':query})
        elif 'see_all' in request.POST:
            all=items()
            return render(request,'inventory/invent.html',{'form':var,'key':all})

    else:
         var=name()
    return render(request,'inventory/invent.html',{'form':var})
