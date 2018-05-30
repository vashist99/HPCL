from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/employee/login/')
def items(request):
    return render(request,'inventory/invent.html')
