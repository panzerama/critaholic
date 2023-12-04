from django.urls import path
from initiative import views


urlpatterns = [
    path('<int:id>/', views.view_init, name='view'),
    path('<int:id>/<int:hp_value>/hp_add', views.hp_add, name='hp add'),
    path('<int:id>/<int:hp_value>/hp_sub', views.hp_sub, name='hp sub'),
    path('new', views.new_init, name='new'),
]