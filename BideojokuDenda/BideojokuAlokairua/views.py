from django.shortcuts import render
from .models import Bideojokua
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    jokuak = Bideojokua.objects.all
    return render(request, 'index.html', {'bideojokua':jokuak}) #ezkerrekoa 'bideojokua' htmlra pasatzen den aldagaiaren izena izango da. 
    