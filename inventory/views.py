from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import items
from .forms import name,HR
from hpemployee.models import hpemployee
from django.forms.formsets import formset_factory,BaseFormSet
from django.forms.models import modelformset_factory
variable=formset_factory(name,formset=BaseFormSet,max_num=5,min_num=2)
variable1=modelformset_factory(items,form=HR,max_num=10,min_num=5,exclude=())

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
        data1={
            'form-TOTAL_FORMS':'3',
            'form-INITIAL_FORMS':'5',
            'form-MAX_NUM_FORMS':'10',
            'form-MIN_NUM_FORMS':'5'
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
                        query=items.objects.filter(item_des=des,locode=locate)
                        #return HttpResponse(query)
                        return render(request,'inventory/invent.html',{'data':q1,'form1':var,'forms':query})


                elif 'see_all' in request.POST:
                    locate=request.session['key']
                    all=items.objects.filter(locode=locate).filter(visibility='yes').filter(visibility='yes').filter(activity='active')
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
            form=variable1(data1)

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
                        query=items.objects.filter(item_des=des,locode=locate)
                            #return HttpResponse(query)

                        query=items.objects.filter(item_des=des).filter(locode=locate)
                        return render(request,'inventory/invent.html',{'data':q1,'form1':var,'forms':query,'form':form})
                elif 'see_all' in request.POST:
                    locate=request.session['key']
                    all=items.objects.filter(locode=locate)
                    return render(request,'inventory/invent.html',{'data':q1,'form1':var,'ha':all,'form':form})
                elif 'update' in request.POST:
                    data3={
                        'form-0-item_des':request.POST,
                        'form-0-item_code':request.POST,
                        'form-0-activity':request.POST,
                        'form-0-quantity':request.POST,
                        'form-0-unit':request.POST,
                        'form-0-visibility':request.POST,
                        'form-0-cost':request.POST,
                        'form-0-pono':request.POST,
                        'form-0-pdate':request.POST,
                        'form-0-inno':request.POST,
                        'form-0-rdate':request.POST}

                    for key in data3:
                        i=request.POST[key]

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
                form=variable1(data)
            return render(request,'inventory/invent.html',{'data':q1,'form1':var,'form':form})
