from django.shortcuts import render
# from django.http import HttpResponse
from initiative.models import Initiative


def home_page(request):
    if request.method == 'POST':
        initiative = Initiative()
        initiative.creature_name = request.POST.get('init_name', '')
        initiative.initiative_value = request.POST.get('init_num', '')
        initiative.save()

    return render(request, 'home.html',
                  {'init_name_text': request.POST.get('init_name', ''),
                   'init_num_text': request.POST.get('init_num', 0)})
