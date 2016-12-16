from django.shortcuts import render, redirect
# from django.http import HttpResponse
from initiative.models import Initiative, Encounter


def home_page(request):
    return render(request, 'home.html')


def init_view(request):
    if request.method == 'POST':
        initiative = Initiative()
        initiative.creature_name = request.POST.get('init_name', '')
        initiative.initiative_value = request.POST.get('init_num', '')
        initiative.save()
        return redirect('/init/the-only-encounter-in-the-world/')

    return render(request, 'init_view.html', {'initiative_order': Initiative.objects.all()})


def new_init(request):
    encounter_ = Encounter.objects.create()
    Initiative.objects.create(creature_name=request.POST['init_name'],
                              initiative_value=request.POST['init_num'],
                              encounter=encounter_)
    return redirect('/init/the-only-encounter-in-the-world/')
