from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import child,reciept
from .forms import HR,reciept
from hpemployee.models import hpemployee
from django.forms.formsets import formset_factory,BaseFormSet
from django.forms.models import modelformset_factory,inlineformset_factory,BaseInlineFormSet

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
                    all=parent.objects.filter(loc=locate).filter(visibility='yes').filter(visibility='yes').filter(activity='active')
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
                        form=reciept()
                        locate=request.session['key']
                        #return HttpResponse(locate)
                        all=child.objects.filter(loc=locate)
                        return render(request,'inventory/invent.html',{'data':q1,'ha':all,'f':r,'reciept':reciept})
                        r.cleaned_data

                elif 'update' in request.POST:
                    r=variable1(data3)
                    form=reciept(request.POST)

                    if form.is_valid():
                        form.save()
                        #return HttpResponse('kjh')

                    if r.is_valid():
                        check=child.objects.filter(item_des=i)
                        for key in data3:
                            i=request.POST[key]
                            #return HttpResponse(i)

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
                    return render(request,'inventory/invent.html',{'data':q1,'f':r,'reciept':reciept})
            else:
                r=variable1(data3)
                form=reciept()
            return render(request,'inventory/invent.html',{'data':q1,'f':r,'reciept':reciept})
