from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import child,reciept
from .forms import HR,rec,itemmaster
from hpemployee.models import hpemployee
from django.forms.formsets import formset_factory,BaseFormSet
from django.forms.models import modelformset_factory,inlineformset_factory,BaseInlineFormSet
from django.core.validators import ValidationError

variable1=modelformset_factory(child,form=HR)


@login_required(login_url='/employee/login/')
def home(request):

    if 'key1' in request.session:
        use=request.session['key1']
        q1=hpemployee.objects.filter(employee_number=use)
        q2=hpemployee.objects.get(employee_number=use)
        data={'form-TOTAL_FORMS':'3',
              'form-INITIAL_FORMS':'3',
              'form-MAX_NUM_FORMS':'5',
              'form-MIN_NUM_FORMS':'2',
              }
        if q2.status=='NHR':
            if request.method=='POST':
                #return HttpResponse(name.__init__())
                if 'logout' in request.POST:
                    logout(request)
                    return redirect('/employee/login/')
                elif 'see_all' in request.POST:
                    locate=request.session['key']
                    all=child.objects.filter(loc=locate).filter(visibility='yes').filter(activity='active')
                    return render(request,'inventory/invent.html',{'data':q1,'ha':all})

            return render(request,'inventory/invent.html',{'data':q1})

        elif q2.status=='HR':

            data3={
                 'form-TOTAL_FORMS':'2',
                 'form-INITIAL_FORMS':'2',
                 'form-MAX_NUM_FORMS':'5',
                 'form-MIN_NUM_FORMS':'2',
                 }
            if request.method=='POST':

                if 'logout' in request.POST:
                    logout(request)
                    return redirect('/employee/login/')

                elif 'see_all' in request.POST:
                    r=variable1(data3)
                    if 'key' in request.session:
                        rep=rec()
                        locate=request.session['key']
                        #return HttpResponse(locate)
                        all=child.objects.filter(loc=locate)
                        return render(request,'inventory/invent.html',{'data':q1,'ha':all,'f':r,'reciept':rep})
                        r.cleaned_data

                elif 'update' in request.POST:
                    r=variable1(data=request.POST,files=request.FILES)
                    rep=rec(request.POST)
                    recie=request.POST['num']
                    if 'key' in request.session:
                        locate=request.session['key']
                    if rep.is_valid():
                        recie1=reciept.objects.filter(num=recie,locode=locate)
                        if not recie1:
                            rep.save()
                        else:
                            raise ValidationError('a reciept by the same number already exists at this location please enter the unique recieptnumber')
                        #return HttpResponse('kjh')
                    if variable1.is_valid():
                        if r in variable1():
                            if r.is_valid():
                                return HttpResponse('valid')
                                check=child.objects.filter(item_des=i)

                                if not check:
                                    r.save()
                                    #return HttpResponse('haha')
                                    if 'key' in request.session:
                                        #return HttpResponse('olalal')
                                        #return HttpResponse('hakunamataa')
                                        child.objects.filter(item_des=i).update(loc=request.session['key'],activity='active')
                                else:
                                    if 'key'in request.session:
                                        b=request.POST['item_code']
                                        c=request.POST['activity']
                                        d=request.POST['quantity']
                                        e=request.POST['cost']
                                        f=request.POST['unit']
                                        g=request.POST['visibility']
                                        i=request.POST['rec_no']
                                        child.objects.filter(item_des=i).update(item_code=b,activity='active',cost=e,recno=i,loc=request.session['key'],visibilitty=g)
                    else:
                        return HttpResponse('hahaha')
                    return render(request,'inventory/invent.html',{'data':q1,'f':r,'reciept':rep})

                elif 'master' in request.POST:
                    return redirect('/inventory/itemmaster/')

            else:
                ch=child()
                #return HttpResponse(request.GET)
                r=variable1(data3)
                rep=rec()
            return render(request,'inventory/invent.html',{'data':q1,'f':r,'reciept':rep,'ch':ch})


def master(request):
    #return HttpReponse('smdjfk')
    if request.method=='POST':
        new=itemmaster(request.POST)
        if new.is_valid():
            new.save()
        else:
            return HttpResponse('invalid entry')
        return render(request,'inventory/master.html',{'item':new})
    elif request.method=='GET':
        new=itemmaster()
    return render(request,'inventory/master.html',{'item':new})
