from django.shortcuts import render, redirect
# from django.http import HttpResponse
from initiative.models import Initiative


def home_page(request):
    if request.method == 'POST':
        initiative = Initiative()
        initiative.creature_name = request.POST.get('init_name', '')
        initiative.initiative_value = request.POST.get('init_num', '')
        initiative.save()
        return redirect('/init/the-only-encounter-in-the-world/')

    return render(request, 'home.html',
                  {'initiative_order': Initiative.objects.all()})


def init_view(request):
    return render(request, 'init_view.html', {'initiative_order': Initiative.objects.all()})
