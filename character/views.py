from django.shortcuts import render, redirect
from character.models import Character


def char_page(request):
    return render(request, 'char_home.html')

def view_char(request, character_id):
    pass

def new_char(request):
    character_ = Character.objects.create()
    return redirect(character_)