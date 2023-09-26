from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    postak = Post.objects.all
    return render(request, 'index.html', {'posta':postak}) #ezkerrekoa htmlra pasatzen den aldagaia da

def add(request):
    return render(request, 'add.html')

def addpost(request):
    iz = request.POST["izenburua"]
    ed = request.POST["edukia"]
    postberria = Post(izenburua = iz, edukia = ed, noizsortua = "")
    postberria.save()
    return HttpResponseRedirect(reverse('index'))

def ezabatu(request, id):
   ezabatzekopost = Post.objects.get(id = id)
   ezabatzekopost.delete()
   return HttpResponseRedirect(reverse('index'))

def eguneratuform(request, id):
    eguneratzekopost = Post.objects.get(id = id)
    return render(request, 'eguneratuform.html', {'posta':eguneratzekopost})


def eguneratu(request, id):
    eguneratzekopost = Post.objects.get(id = id)
    iz = request.POST["izenburua"]
    ed = request.POST["edukia"]
    eguneratzekopost.izenburua = iz
    eguneratzekopost.edukia = ed
    eguneratzekopost.save()

    return HttpResponseRedirect(reverse('index'))

