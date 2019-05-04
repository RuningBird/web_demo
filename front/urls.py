
from django.contrib import admin
from django.urls import path
from front import views

urlpatterns = [
    path('capacity/', views.capacity_distribution, name='capacity_distribution'),
    path('capacity/grow/', views.capacity_grow, name='capacity_grow'),
    path('', views.index, name='index'),
    path('person/ships/', views.persion_work_ship_info, name='persion_word_ship_info'),

    path('json/capacity/', views.json_capacity_distribution, name='json_capacity_distribution'),
    path('json/person/ships/', views.json_persion_work_ship_info, name='json_persion_word_ship_info'),

]
