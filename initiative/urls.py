from django.conf.urls import url
from django.contrib import admin
from initiative import views


urlpatterns = [
    url(r'^(\d+)/$', views.view_init, name='view'),
    url(r'^(\d+)/add_init', views.add_init, name='add'),
    url(r'^new$', views.new_init, name='new'),
]