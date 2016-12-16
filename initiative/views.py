from django.shortcuts import render, redirect
# from django.http import HttpResponse
from initiative.models import Initiative, Encounter


def home_page(request):
    return render(request, 'home.html')


def init_view(request, encounter_id):
    encounter_ = Encounter.objects.get(id=encounter_id)
    inits = Initiative.objects.filter(encounter=encounter_id)
    return render(request, 'init_view.html', {'initiative_order': inits})


def new_init(request):
    encounter_ = Encounter.objects.create()
    Initiative.objects.create(creature_name=request.POST['init_name'],
                              initiative_value=request.POST['init_num'],
                              encounter=encounter_)
    return redirect('/init/%d/' % (encounter_.id))
