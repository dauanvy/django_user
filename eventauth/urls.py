from django.conf.urls import *
from django.conf import settings
from eventauth import views as eventauth_views

urlpatterns = [
    url(r'^$',eventauth_views.index,name='index'),
	url(r'^users$', eventauth_views.users, name='users'),
	url(r'^success$', eventauth_views.success, name='success'),
	url(r'^groups$', eventauth_views.groups, name='groups'),
	url(r'^base_admin$', eventauth_views.base_admin, name='base_admin'),
]