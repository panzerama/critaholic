from django.conf.urls import url
from character import views


urlpatterns = [
    url(r'^$', views.char_page, name='character home'),
    url(r'^(\d+)/$', views.view_char, name='character view'),
    url(r'^new$', views.new_char, name='new char'),
]