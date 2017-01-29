from django.conf.urls import url
from django.contrib import admin
from initiative import views


urlpatterns = [
    url(r'^$', views.home_page, name='init home'),
    url(r'^(\d+)/$', views.view_init, name='init view'),
    url(r'^(\d+)/(\d+)/hp_add', views.hp_add, name='hp add'),
    url(r'^(\d+)/(\d+)/hp_sub', views.hp_sub, name='hp sub'),
    url(r'^new$', views.new_init, name='new'),
]