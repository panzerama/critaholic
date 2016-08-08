from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

def home_page(request):
	return render(request, 'home.html', 
		{'init_name_text': request.POST.get('init_name', ''), 'init_num_text': request.POST.get('init_num', '')})
