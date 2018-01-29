from django.db import models
# Create your models here.
from django import forms

class EventUsers(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=256, default='')
	password = models.CharField(max_length=256, default='')
	email = models.CharField(max_length=256, default='')
	class Meta:
		db_table = "eventusers"
		ordering = ['-id']
class EventUsersForm(forms.ModelForm):
	username = forms.CharField(label= 'User Name', max_length=100, strip=True)
	password = forms.CharField(label= 'Password', max_length=100, strip=True)
	email = forms.CharField(label= 'Email', max_length=100, strip=True)
	class Meta:
		model = EventUsers
		fields = ['username', 'password', 'email']

class EventGroups(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=256, default='')
	class Meta:
		db_table = "eventgroups"
		ordering = ['-id']
class EventGroupsForm(forms.ModelForm):
	name = forms.CharField(label= 'Name', max_length=100, strip=True)
	class Meta:
		model = EventGroups
		fields = ['name']
	