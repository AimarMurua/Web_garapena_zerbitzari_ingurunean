from django.shortcuts import render
from .models import Mahaia
from .models import Bezeroa
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    bezeroa = Bezeroa.objects.all
    return render(request, 'index.html', {'bezeroak':bezeroa})

def gehitu(request):
    return render(request, 'gehitu.html')

def gehitubezeroa(request):
    dni = request.POST['dni']
    izena = request.POST['izena']
    abizena = request.POST['abizena']

    bezeroa = Bezeroa(dni = dni, izena = izena, abizena = abizena)
    bezeroa.save()
    return HttpResponseRedirect(reverse('index'))

def ezabatubezeroa(request, dni):
    bezeroa = Bezeroa.objects.get(dni = dni)
    bezeroa.delete()
    return HttpResponseRedirect(reverse('index'))