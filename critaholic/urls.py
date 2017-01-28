"""critaholic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from critaholic import views as base_views

from initiative import views as init_views
from initiative import urls as init_urls

from character import urls as character_urls


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', base_views.home_page, name='home'),
    url(r'^init/', include(init_urls)),
    url(r'^character/', include(character_urls))
]
