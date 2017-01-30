from django.shortcuts import render, redirect
from character.models import Character


def char_page(request):
    return render(request, 'home.html')


def view_char(request, character_id):
    character_ = Character.objects.get(id=character_id)
    return render(request, 'view_char.html', {'character': character_})


def new_char(request):
    character_ = Character.objects.create(character_name=request.POST['character_name'],
                                          summary=request.POST['character_description'])
    character_.full_clean()
    character_.save()
    return redirect(character_)