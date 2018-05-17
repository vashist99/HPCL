from django.shortcuts import render
from .models import hpemployee


def employeepage(request):
    var = hpemployee.objects.all().order_by("employee_name")
    return render(request,'hpemployee\homepage.html',{"key":var})

# Create your views here.
