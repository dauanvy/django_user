from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, Http404
<<<<<<< HEAD
from eventauth.models import EventUsers, EventUsersForm

def index(request):
	return render(request,'home.html')
def success(request):
	return render(request,'success.html')
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
	return render(request, 'users.html')
=======


def index(request):
	return render(request,'home.html')
>>>>>>> a413f29ca018116edf7a3ed06a0b9b0ac17492fc
