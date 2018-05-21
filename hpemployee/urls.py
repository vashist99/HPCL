
from django.conf.urls import url
from . import views


urlpatterns = [
url(r'^$',views.employeepage),
url(r'hpemployee/$',views.employeedetails),
]
