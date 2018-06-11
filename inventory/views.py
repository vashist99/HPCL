from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import child,reciept
from .forms import name,HR,reciept
from hpemployee.models import hpemployee
from django.forms.formsets import formset_factory,BaseFormSet
from django.forms.models import modelformset_factory,inlineformset_factory,BaseInlineFormSet
variable=formset_factory(name,formset=BaseFormSet,max_num=5,min_num=2)
variable1=modelformset_factory(child,form=HR,max_num=10,min_num=5,exclude=())

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

        var=variable(data)

        if q2.status=='NHR':
            if request.method=='POST':
                #return HttpResponse(name.__init__())
                if 'logout' in request.POST:
                    logout(request)
                    return redirect('/employee/login/')
                elif 'see' in request.POST:
                    data2={
                         'form-0-item_name':request.POST,
                         }
                    if 'key' in request.session:
                        #return HttpResponse(des)
                        locate=request.session['key']
                    #return HttpResponse(request.POST)
                    for key in data2:
                        des=request.POST[key]
                        #return HttpResponse(des)
                        #return HttpResponse(key)
                        #return HttpResponse(locate)
                        query=child.objects.filter(item_des=des,locode=locate)
                        #return HttpResponse(query)
                        return render(request,'inventory/invent.html',{'data':q1,'form1':var,'forms':query})


                elif 'see_all' in request.POST:
                    locate=request.session['key']
                    all=parent.objects.filter(locode=locate).filter(visibility='yes').filter(visibility='yes').filter(activity='active')
                    return render(request,'inventory/invent.html',{'data':q1,'form1':var,'ha':all})
            else:
                #return HttpResponse(name.__init__())
                data={'form-TOTAL_FORMS':'3',
                      'form-INITIAL_FORMS':'2',
                      'form-MAX_NUM_FORMS':'5',
                      'form-MIN_NUM_FORMS':'2',}
                var=variable(data)
            return render(request,'inventory/invent.html',{'data':q1,'form1':var})

        elif q2.status=='HR':
            r=variable1()
            if request.method=='POST':
                if 'logout' in request.POST:
                    logout(request)
                    return redirect('/employee/login/')
                elif 'see' in request.POST:
                    data2={
                         'form-0-item_name':request.POST,
                         }
                    if 'key' in request.session:
                        #return HttpResponse(des)
                        locate=request.session['key']
                        #return HttpResponse(request.POST)
                    for key in data2:
                        des=request.POST[key]
                        #return HttpResponse(des)
                        #return HttpResponse(key)
                        #return HttpResponse(locate)
                        query=child.objects.filter(item_des=des,locode=locate)
                        #return HttpResponse(query)
                        query=child.objects.filter(item_des=des).filter(locode=locate)
                        return render(request,'inventory/invent.html',{'data':q1,'form1':var,'forms':query,'forms':form,'form':r})
                elif 'see_all' in request.POST:
                    locate=request.session['key']
                    all=child.objects.filter(locode=locate)
                    return render(request,'inventory/invent.html',{'data':q1,'form1':var,'ha':all,'forms':form,'form':r})
                elif 'update' in request.POST:
                    r=reciept(request.POST)
                    data3={
                        'form-0-item_code':request.POST,
                        'form-0-item_des':request.POST,
                        'form-0-activity':request.POST,
                        'form-0-quantity':request.POST,
                        'form-0-unit':request.POST,
                        'form-0-visibility':request.POST,
                        }
                    for key in data3:
                        i=request.POST[key]
                        check=child.objects.filter(item_des=i)
                        if not check:
                            if 'key' in request.session:
                                r.save()
                                child.objects.filter(item_des=i)
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
                                child.objects.filter(item_des=i).update(item_code=b,activity=c,quantity=d,cost=e,unit=f,visibility=g,pdate=i,rdate=h,pono=j,inno=k)
            else:
                r=variable1()
                form=reciept()
            return render(request,'inventory/invent.html',{'data':q1,'form1':var,'forms':r,'form':form})
