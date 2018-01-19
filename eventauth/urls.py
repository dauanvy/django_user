from django.conf.urls import *
from django.conf import settings
from eventauth import views as eventauth_views

urlpatterns = [
    url(r'^$',eventauth_views.index,name='index'),
<<<<<<< HEAD
	url(r'^users$', eventauth_views.users, name='users'),
	url(r'^success$', eventauth_views.success, name='success'),
=======
>>>>>>> a413f29ca018116edf7a3ed06a0b9b0ac17492fc
]