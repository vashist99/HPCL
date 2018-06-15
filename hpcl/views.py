from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request,'homepage.html')
def about(request):
    return render(request,'about.html')
def test(request):
    return HttpResponse('welcome to HPCL')
