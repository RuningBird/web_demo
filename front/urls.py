
from django.contrib import admin
from django.urls import path
from front import views

urlpatterns = [
    path('capacity/', views.capacity_distribution, name='capacity_distribution'),
    path('capacity/grow/', views.capacity_grow, name='capacity_grow'),
    path('', views.index, name='index'),

    path('json/capacity/', views.json_capacity_distribution, name='json_capacity_distribution'),

]
