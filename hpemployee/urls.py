
from django.conf.urls import url
from . import views



urlpatterns = [
url(r'^$',views.employeepage,name='emp_homepage'),
url(r'hpemployee/$',views.employeedetails, name='emp_details'),
url(r'login/$',views.log,name='login'),
]
