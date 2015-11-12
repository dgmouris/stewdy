from django.conf import settings
from django.shortcuts import render

def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)