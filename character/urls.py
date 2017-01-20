from django.conf.urls import url
from character import views


urlpatterns = [
    url(r'^$', views.char_page, name='character view'),
]