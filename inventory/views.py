from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
from django.http import HttpResponse
from .models import child,reciept
from .forms import HR,rec,itemmaster
from hpemployee.models import hpemployee
from django.forms.formsets import formset_factory,BaseFormSet
from django.forms.models import modelformset_factory,inlineformset_factory,BaseInlineFormSet
from django.core.validators import ValidationError

@login_required(login_url='/employee/login/')
def baseinvent(request):
    if 'key1' in request.session :
        use=request.session['key1']
        q1=hpemployee.objects.filter(employee_number=use)
    if request.method=='POST':
        if 'logout' in request.POST:
            logout(request)
            return redirect('/employee/login/')
        elif 'inventory' in request.POST:
            #return HttpResponse(request.POST)
            #login(request,user)
            #logout(request)
            return redirect('/inventory/viewinvent/')
        elif 'itemmaster' in request.POST:
            #login(request,user)
            #logout(request)
            return redirect('/inventory/itemmaster/')
    else:
        return render(request,'inventory/baseinvent.html',{'key':q1})

@login_required(login_url='/employee/login/')
def home(request):
    if 'key1' in request.session:
        use=request.session['key1']
        q2=hpemployee.objects.get(employee_number=use)

        if q2.status=='NHR':
            if request.method=='POST':
                #return HttpResponse(name.__init__())
                if 'logout' in request.POST:
                    logout(request)
                    return redirect('/employee/login/')

                elif 'see_all' in request.POST:
                    locate=request.session['key']
                    all=child.objects.filter(loc=locate).filter(visibility='yes').filter(activity='active')
                    return render(request,'inventory/invent.html',{'ha':all})

            return render(request,'inventory/invent.html')

        elif q2.status=='HR':
            que=child.objects.filter(loc=request.session['key'])
            variable1=modelformset_factory(child,form=HR)

            data3={
                 'form-TOTAL_FORMS':'2',
                 'form-MAX_NUM_FORMS':'5',
                 'form-MIN_NUM_FORMS':'2'
                     }

            if request.method=='POST':

                if 'see_all' in request.POST:
                    if 'key' in request.session:
                        r=variable1()
                        rep=rec()
                        locate=request.session['key']
                        #return HttpResponse(locate)
                        all=child.objects.filter(loc=locate)
                        return render(request,'inventory/invent.html',{'ha':all,'f':r,'reciept':rep})
                        r.cleaned_data

                    elif 'update' in request.POST:
                        #return HttpResponse(request.POST)
                        r=variable1(request.POST)
                        return HttpResponse(r)
                        rep=rec(request.POST)
                        recie=request.POST['num']
                        locate=request.session['key']
                        if rep.is_valid():
                            recie1=reciept.objects.filter(num=recie,locode=locate)
                            if not recie1:
                                rep.save()
                            else:
                                raise ValidationError('a reciept by the same number already exists at this location please enter the unique recieptnumber')
                                #return HttpResponse('kjh')

                                if r.is_valid():
                                    return HttpResponse('valid ')
                                    if form in r:
                                        if form.is_valid():
                                            return HttpResponse('valid')
                                            c=request.POST['activity']
                                            d=request.POST['quantity']
                                            e=request.POST['cost']
                                            i=request.POST['rec_no']
                                            child.objects.filter(item_des=i,loc=locate).update(quantity=d,activity='active',cost=e,recno=i)
                                            #else:
                                            #return HttpResponse('hahaha')
                                            return render(request,'inventory/invent.html',{'f':r,'reciept':rep})
            else:
                r=variable1()
                rep=rec()
            return render(request,'inventory/invent.html',{'f':r,'reciept':rep})

def master(request):
    if 'key1' not in request.session:
        return redirect('/employee/login/')

    if request.method=='POST':
        new=itemmaster(request.POST)
        if new.is_valid():
            new.save()
        else:
            return HttpResponse('invalid entry')
        return render(request,'inventory/master.html',{'item':new})
    else:
        new=itemmaster()
    return render(request,'inventory/master.html',{'item':new})

    #print('welcome')
    #return HttpReponse('smdjfk')
