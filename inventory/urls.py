from django.conf.urls import url
from . import views

urlpatterns=[
url(r'$',views.home,name='invent'),
url(r'itemmaster$',views.master,name='master'),
]
