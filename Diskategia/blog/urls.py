from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('add/', views.add, name = 'add'),
    path('add/addpost/', views.addpost, name = 'addpost'),
    path('ezabatu/<int:id>', views.ezabatu, name = 'ezabatu'),
    path('eguneratuform/<int:id>', views.eguneratuform, name = 'eguneratuform'),
    path('eguneratu/<int:id>', views.eguneratu, name = 'eguneratu')
]