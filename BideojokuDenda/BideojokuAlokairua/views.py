from django.shortcuts import render
from .models import Bideojokua
from .models import Bezeroa
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    jokuak = Bideojokua.objects.all
    return render(request, 'index.html', {'bideojokua':jokuak}) #ezkerrekoa 'bideojokua' htmlra pasatzen den aldagaiaren izena izango da. 

def bezeroak(request):
    bezeroak = Bezeroa.objects.all
    return render(request, 'bezeroak.html', {'bezeroa':bezeroak})

def add(request):
    return render(request, 'addbid.html')

def addbez(request):
    return render(request, 'addbez.html')

def addbid(request):
    bid_id = request.POST["bid_id"]
    bid_izena = request.POST["bid_izena"]
    bid_generoa = request.POST["bid_generoa"]
    bid_hizkuntza = request.POST["bid_hizkuntza"]
    bid_irteeradata = request.POST["bid_irteeradata"]
    bid_adinminimoa = request.POST["bid_adinminimoa"]
    bid_sinopsia = request.POST["bid_sinopsia"]

    bid_berria = Bideojokua(
                    bid_id = bid_id,
                    bid_izena = bid_izena, 
                    bid_generoa = bid_generoa, 
                    bid_hizkuntza = bid_hizkuntza, 
                    bid_irteeradata = bid_irteeradata, 
                    bid_adinminimoa = bid_adinminimoa, 
                    bid_sinopsia = bid_sinopsia
                )
    bid_berria.save()
    return HttpResponseRedirect(reverse('index'))

def addbezero(request):
    bez_dni = request.POST["bez_dni"]
    bez_izena = request.POST["bez_izena"]
    bez_abizena = request.POST["bez_abizena"]
    bez_telefonoa = request.POST["bez_telefonoa"]
    bez_email = request.POST["bez_email"]
    bez_helbidea = request.POST["bez_helbidea"]

    bez_berria = Bezeroa(
                    bez_dni = bez_dni,
                    bez_izena = bez_izena,
                    bez_abizena = bez_abizena,
                    bez_telefonoa = bez_telefonoa, 
                    bez_email = bez_email, 
                    bez_helbidea = bez_helbidea
                )
    bez_berria.save()
    return HttpResponseRedirect(reverse('bezeroak'))

def ezabatubid(request, id):
    ezabatzekobideojokua = Bideojokua.objects.get(id = id)
    ezabatzekobideojokua.delete()
    return HttpResponseRedirect(reverse('index'))

def ezabatubez(request, id):
    ezabatzekobezeroa = Bezeroa.objects.get(id = id)
    ezabatzekobezeroa.delete()
    return HttpResponseRedirect(reverse('bezeroak'))

def eguneratubidform(request, id): 
    eguneratzekobideojokua = Bideojokua.objects.get(id = id)
    return render(request, 'eguneratubidform.html', {'bideojokua':eguneratzekobideojokua})

def eguneratubid(request, id): 
    eguneratzekobid = Bideojokua.objects.get(id = id)
    bid_id = request.POST["bid_id"]
    bid_izena = request.POST["bid_izena"]
    bid_generoa = request.POST["bid_generoa"]
    bid_hizkuntza = request.POST["bid_hizkuntza"]
    bid_irteeradata = request.POST["bid_irteeradata"]
    bid_adinminimoa = request.POST["bid_adinminimoa"]
    bid_sinopsia = request.POST["bid_sinopsia"]

    eguneratzekobid.bid_id = bid_id
    eguneratzekobid.bid_izena = bid_izena
    eguneratzekobid.bid_generoa = bid_generoa
    eguneratzekobid.bid_hizkuntza = bid_hizkuntza
    eguneratzekobid.bid_irteeradata = bid_irteeradata
    eguneratzekobid.bid_adinminimoa = bid_adinminimoa
    eguneratzekobid.bid_sinopsia = bid_sinopsia
    eguneratzekobid.save()

    return HttpResponseRedirect(reverse('index'))
