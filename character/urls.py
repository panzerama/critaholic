from django.urls import path
from character import views


urlpatterns = [
    path(r'^$', views.char_page, name='character home'),
    path(r'^(\d+)/$', views.view_char, name='character view'),
    path(r'^new$', views.new_char, name='new char'),
]