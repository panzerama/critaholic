from django.urls import path
from initiative import views


urlpatterns = [
    path(r'^(\d+)/$', views.view_init, name='view'),
    path(r'^(\d+)/(\d+)/hp_add', views.hp_add, name='hp add'),
    path(r'^(\d+)/(\d+)/hp_sub', views.hp_sub, name='hp sub'),
    path(r'^new$', views.new_init, name='new'),
]