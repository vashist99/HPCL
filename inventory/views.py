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
variable1=modelformset_factory(child,form=HR,max_num=5,min_num=4,exclude=())

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
                        query=child.objects.filter(item_des=des,loc=locate)
                        #return HttpResponse(query)
                        return render(request,'inventory/invent.html',{'data':q1,'form1':var,'forms':query})


                elif 'see_all' in request.POST:
                    locate=request.session['key']
                    all=parent.objects.filter(loc=locate).filter(visibility='yes').filter(visibility='yes').filter(activity='active')
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
                    form=reciept()
                #    data2={
                #         'form-0-item_name':'',
                #         'form-1-item_name':'',
                #         'form-2-item_name':''
                #         }
                    if 'key' in request.session:
                        #return HttpResponse(des)
                        locate=request.session['key']
                        #return HttpResponse(request.POST)
                        des1=request.POST['form-0-item_name']
                        des2=request.POST['form-1-item_name']
                        des3=request.POST['form-2-item_name']
                        #return HttpResponse(des3)
                        #return HttpResponse(des2)
                        #return HttpResponse(des1)
                        #return HttpResponse(key)
                        #return HttpResponse(locate)
                        query1=child.objects.filter(item_des=des1).filter(loc=locate)
                        query2=child.objects.filter(item_des=des2).filter(loc=locate)
                        query3=child.objects.filter(item_des=des3).filter(loc=locate)
                        #return HttpResponse(query3)
                        #return HttpResponse(query2)
                        #return HttpResponse(query1)
                        return render(request,'inventory/invent.html',{'data':q1,'form1':var,'forms':query1,'forms':query2,'forms':query3,'key':r,'form':form})
                elif 'see_all' in request.POST:
                    if 'key' in request.session:
                        form=reciept()
                        locate=request.session['key']
                        #return HttpResponse(locate)
                        all=child.objects.filter(loc=locate)
                        return render(request,'inventory/invent.html',{'data':q1,'form1':var,'ha':all,'key':r,'form':form})

                elif 'update' in request.POST:
                    form=reciept(request.POST)
                    data3={
                        'form-0-item_code':'',
                        'form-0-item_des':'',
                        'form-0-activity':'',
                        'form-0-quantity':'',
                        'form-0-unit':'',
                        'form-0-visibility':'',
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
            return render(request,'inventory/invent.html',{'data':q1,'form1':var,'key':r,'form':form})
