from django.urls import path
from character import views


urlpatterns = [
    path('', views.char_page, name='character home'),
    path('<int:id>/view', views.view_char, name='character view by id'),
    path('new', views.new_char, name='new char'),
]