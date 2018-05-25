
from django.conf.urls import url
from . import views


urlpatterns = [
url(r'^$',views.employeepage,name="emp_home"),
url(r'hpemployee/$',views.employeedetails,name="emp_det"),
]
