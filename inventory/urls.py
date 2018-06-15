from django.conf.urls import url
from . import views

urlpatterns=[
url(r'$',views.baseinvent,name='baseinvent'),
url(r'viewinvent/$',views.home,name='invent'),
url(r'itemmaster/$',views.master),
#url(r'test/$',views.test)
]
