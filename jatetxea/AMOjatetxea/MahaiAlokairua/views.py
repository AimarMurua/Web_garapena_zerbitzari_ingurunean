from django.shortcuts import render
from .models import Mahaia
from .models import Bezeroa
from .models import Alokairua
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

def eguneratubezeroa(request, dni):
    bezeroa = Bezeroa.objects.get(dni = dni)
    return render(request, 'eguneratubezeroa.html', {'bezeroa':bezeroa})

def eguneratubezeroaerregistroa(request, dni): 
    dni = request.POST['dni']
    izena = request.POST['izena']
    abizena = request.POST['abizena']

    bezeroa = Bezeroa.objects.get(dni = dni)
    bezeroa.dni = dni
    bezeroa.izena = izena
    bezeroa.abizena = abizena

    bezeroa.save()
    return HttpResponseRedirect(reverse('index'))

def alokairua(request):
    alokairuak = Alokairua.objects.all
    return render(request, 'alokairuak.html', {'alokairua':alokairuak})

def gehitualokairua(request):
    bezeroa = Bezeroa.objects.all
    mahaia = Mahaia.objects.all

    return render(request, 'gehitualokairua.html', {'bezeroa':bezeroa, 'mahaia':mahaia})

def gehitualokairuaerregistroa(request): 
    mahaia = request.POST['mahai_zenbakia']
    mahaiaOndo = Mahaia.objects.get(zenbakia = mahaia)

    bezeroa = request.POST['bezero_dni']
    bezeroaOndo = Bezeroa.objects.get(izena = bezeroa)

    alokairuData = request.POST['alokairu_data']
    alokairuOrdua = request.POST['alokairu_ordua']

    alokairua = Alokairua(mahai_zenbakia = mahaiaOndo, bezero_dni = bezeroaOndo, alokairu_data = alokairuData, alokairu_ordua = alokairuOrdua)
    alokairua.save()
    return HttpResponseRedirect(reverse('index'))