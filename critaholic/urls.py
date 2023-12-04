from django.urls import include, path
from initiative import views as init_views

from initiative import urls as init_urls
from character import urls as character_urls


urlpatterns = [
    path('', init_views.home_page, name='home'),
    path('init/', include(init_urls)),
    path('character/', include(character_urls))
]
