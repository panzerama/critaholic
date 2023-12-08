from django.urls import path
from initiative import views


urlpatterns = [
    path('<int:encounter_id>/', views.view_init, name='view'),
    path('<int:encounter_id>/<int:initiative_id>/hp_add', views.hp_add, name='hp add'),
    path('<int:encounter_id>/<int:initiative_id>/hp_sub', views.hp_sub, name='hp sub'),
    path('new', views.new_init, name='new'),
]