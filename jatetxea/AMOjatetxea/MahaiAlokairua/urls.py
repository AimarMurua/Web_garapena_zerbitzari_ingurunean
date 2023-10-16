from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('gehitu/', views.gehitu, name = 'gehitu'),
    path('gehitu/gehitubezeroa/', views.gehitubezeroa, name = 'gehitubezeroa'),
    path('ezabatubezeroa/<dni>', views.ezabatubezeroa, name = 'ezabatubezeroa'),
    path('eguneratubezeroa/<dni>', views.eguneratubezeroa, name = 'eguneratu'),
    path('eguneratubezeroa/eguneratubezeroaerregistroa/<dni>', views.eguneratubezeroaerregistroa, name='eguneratubezeroaerregistroa'), 
    path('alokairua/', views.alokairua, name = 'alokairua'),
    path('alokairua/gehitualokairua/', views.gehitualokairua, name = 'gehitualokairua'),
    path('alokairua/gehitualokairua/gehitualokairuaerregistroa/', views.gehitualokairuaerregistroa, name = 'gehitualokairuaerregistroa'),
]