from django.shortcuts import render
from .models import Bideojokua
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    jokuak = Bideojokua.objects.all
    return render(request, 'index.html', {'bideojokua':jokuak}) #ezkerrekoa 'bideojokua' htmlra pasatzen den aldagaiaren izena izango da. 

def add(request):
    return render(request, 'addbid.html')

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