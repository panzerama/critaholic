from django.shortcuts import render, redirect
# from django.http import HttpResponse
from initiative.models import Initiative, Encounter
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError


def home_page(request):
    return render(request, 'home.html')


def view_init(request, encounter_id):
    encounter_ = Encounter.objects.get(id=encounter_id)
    error = None
    if request.method == 'POST':
        try:
            initiative_ = Initiative.objects.create(creature_name=request.POST['init_name'],
                                  initiative_value=request.POST['init_num'],
                                  hit_points=request.POST['init_hp'],
                                  encounter=encounter_)
            initiative_.full_clean()
            initiative_.save()
            return redirect(encounter_)
        except ValidationError:
            initiative_.delete()
            error = 'An initiative entry must have a name!'
        except ValueError:
            error = 'An initiative entry must have a valid initiative value!'
    return render(request, 'view_init.html', {'encounter': encounter_, 'error': error})


def new_init(request):
    encounter_ = Encounter.objects.create()

    try:
        initiative_ = Initiative.objects.create(creature_name=request.POST['init_name'],
                                                initiative_value=request.POST['init_num'],
                                                hit_points=request.POST['init_hp'],
                                                encounter=encounter_)
        initiative_.full_clean()
        initiative_.save()
    except ValidationError:
        encounter_.delete()
        error = 'An initiative entry must have a name!'
        return render(request, 'home.html', {'error': error})
    except ValueError:
        encounter_.delete()
        error = 'An initiative entry must have a valid initiative value!'
        return render(request, 'home.html', {'error': error})

    return redirect(encounter_)


def hp_add(request, encounter_id, initiative_id):
    initiative_ = Initiative.objects.get(id=initiative_id)
    initiative_name = initiative_.creature_name
    hp_amount = int(request.POST['%s_hp_value' % (initiative_name,)])
    initiative_.hit_points += hp_amount
    initiative_.save()

    return redirect(Encounter.objects.get(id=encounter_id))


def hp_sub(request, encounter_id, initiative_id):
    initiative_ = Initiative.objects.get(id=initiative_id)
    initiative_name = initiative_.creature_name
    hp_amount = int(request.POST['%s_hp_value' % (initiative_name,)])
    initiative_.hit_points -= hp_amount
    initiative_.save()

    return redirect(Encounter.objects.get(id=encounter_id))