from django.shortcuts import render, redirect
# from django.http import HttpResponse
from initiative.models import Initiative, Encounter


def home_page(request):
    return render(request, 'home.html')


def view_init(request, encounter_id):
    encounter_ = Encounter.objects.get(id=encounter_id)
    return render(request, 'view_init.html', {'encounter': encounter_})


def new_init(request):
    encounter_ = Encounter.objects.create()
    Initiative.objects.create(creature_name=request.POST['init_name'],
                              initiative_value=request.POST['init_num'],
                              hit_points=request.POST['init_hp'],
                              encounter=encounter_)
    return redirect('/init/%d/' % (encounter_.id))


def add_init(request, encounter_id):
    encounter_ = Encounter.objects.get(id=encounter_id)
    Initiative.objects.create(creature_name=request.POST['init_name'],
                              initiative_value=request.POST['init_num'],
                              hit_points=request.POST['init_hp'],
                              encounter=encounter_)
    return redirect('/init/%d/' % (encounter_.id,))


def hp_add(request, encounter_id, initiative_id):
    initiative_ = Initiative.objects.get(id=initiative_id)
    initiative_name = initiative_.creature_name
    hp_amount = int(request.POST[initiative_name + '_hp_value'])
    initiative_.hit_points += hp_amount
    initiative_.save()

    return redirect('/init/%s/' % (encounter_id))


def hp_sub(request, encounter_id, initiative_id):
    return redirect('/init/%s/' % (encounter_id))