from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db import models

def home(request):		
	return render(request, 'home.html')
	
def scout(request):
	return render(request, 'scout.html')

def data(request):
	return render(request, 'data.html')