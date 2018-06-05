from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import items
from .forms import name,HR
from hpemployee.models import hpemployee

@login_required(login_url='/employee/login/')
def home(request):

    if 'key1' in request.session:
        use=request.session['key1']
        q1=hpemployee.objects.filter(employee_number=use)
        q2=hpemployee.objects.get(employee_number=use)

        if q2.status=='NHR':
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
                        return render(request,'inventory/invent.html',{'data':q1,'form1':var,'forms':query})
                elif 'see_all' in request.POST:
                    locate=request.session['key']
                    all=items.objects.filter(locode=locate).filter(visibility='yes').filter(visibility='yes').filter(activity='active')
                    return render(request,'inventory/invent.html',{'data':q1,'form1':var,'ha':all})
            else:
                var=name()
                return render(request,'inventory/invent.html',{'data':q1,'form1':var})
        elif q2.status=='HR':

            if request.method=='POST':
                var=name()
                form=HR()
                if 'logout' in request.POST:
                    logout(request)
                    return redirect('/employee/login/')
                elif 'see' in request.POST:
                    var=name(request.POST)
                    des=request.POST['item_name']
                    if 'key' in request.session:
                        locate=request.session['key']
                        query=items.objects.filter(item_des=des).filter(locode=locate)
                        return render(request,'inventory/invent.html',{'data':q1,'form1':var,'forms':query,'HR':form})
                elif 'see_all' in request.POST:
                    locate=request.session['key']
                    all=items.objects.filter(locode=locate)
                    return render(request,'inventory/invent.html',{'data':q1,'form1':var,'ha':all,'HR':form})
                elif 'update' in request.POST:
                    form=HR(request.POST)
                    i=request.POST['item_des']
                    check=items.objects.filter(item_des=i)
                    if not check:
                        if 'key' in request.session:
                            form.save()
                            items.objects.filter(item_des=i).update(locode=request.session['key'])
                    else:
                        b=request.POST['item_code']
                        c=request.POST['activity']
                        d=request.POST['quantity']
                        e=request.POST['cost']
                        f=request.POST['unit']
                        g=request.POST['visibility']
                        i=request.POST['pdate']
                        h=request.POST['rdate']
                        j=request.POST['pono']
                        k=request.POST['inno']
                        items.objects.filter(item_des=i).update(item_code=b,activity=c,quantity=d,cost=e,unit=f,visibility=g,pdate=i,rdate=h,pono=j,inno=k)

            else:
                var=name()
                hr=HR()
            return render(request,'inventory/invent.html',{'data':q1,'form1':var,'HR':form})
