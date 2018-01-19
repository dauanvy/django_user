from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, Http404


def index(request):
	return render(request,'home.html')