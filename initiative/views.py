from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	return HttpResponse('<html><title>Critaholic: Initiative Tracker</title><h1>Critaholic: Initiative!</h1></html>')