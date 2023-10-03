from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),

    path('add/', views.add, name = 'add'),
    path('add/addbid/', views.addbid, name = 'addbid'), #form action izena form action="addbid/"

    path('add/addbez/', views.addbez, name= 'addbez'),
    path('add/addbezero/', views.addbezero, name= 'addbezero'),
    path('bezeroak/', views.bezeroak, name = 'bezeroak'),

    path('ezabatubideojokua/<int:id>', views.ezabatubid, name = 'ezabatubid'),
    path('bezeroak/ezabatubezeroa/<int:id>', views.ezabatubez, name = 'ezabatubez'),

    path('eguneratubidform/<int:id>', views.eguneratubidform, name = 'eguneratubidform'),
    path('eguneratubid/<int:id>', views.eguneratubid, name = 'eguneratubid'),

    path('bezeroak/eguneratubezform/<int:id>', views.eguneratubezform, name = 'eguneratubezform'), 
    path('eguneratubez/<int:id>', views.eguneratubez, name = 'eguneratubez')
]   
