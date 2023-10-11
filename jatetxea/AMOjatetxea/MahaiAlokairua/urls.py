from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('gehitu/', views.gehitu, name = 'gehitu'),
    path('gehitu/gehitubezeroa/', views.gehitubezeroa, name = 'gehitubezeroa'),
    path('ezabatubezeroa/<dni>', views.ezabatubezeroa, name = 'ezabatubezeroa'),
]