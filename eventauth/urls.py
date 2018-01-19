from django.conf.urls import *
from django.conf import settings
from eventauth import views as eventauth_views

urlpatterns = [
    url(r'^$',eventauth_views.index,name='index'),
]