from django.shortcuts import render

def char_page(request):
    return render(request, 'char_home.html')