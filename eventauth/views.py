from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, Http404
from eventauth.models import EventUsers, EventUsersForm
from eventauth.models import EventGroups, EventGroupsForm

def index(request):
	return render(request,'home.html')
def success(request):
	return render(request,'success.html')
#User
def users(request):
	data = {}
	if request.method == 'POST':
		form = EventUsersForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/success')
	else:
		form = EventUsersForm()
	list_item = EventUsers.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return render(request, 'users.html', data)
#Group
def groups (request):
	data = {}
	if request.method == 'POST':
		form = EventGroupsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/success')
	else:
		form = EventGroupsForm()
	list_item = EventGroups.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return render(request, 'groups.html', data)