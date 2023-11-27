from django.http import HttpResponse


def home_page(request):
    return HttpResponse("<html><head><title>Initiative Tracker</title></head></html>")