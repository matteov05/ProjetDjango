from django.shortcuts import render, HttpResponseRedirect
from .forms import ContinentForm
from .import models

# Create your views here.
def ajout (request):
    if request.method == "POST":
        form = ContinentForm(request)
        return render(request, "continent/ajout.html", {"form": form})
    else :
        form = ContinentForm()
        return render(request, "continent/ajout.html", {"form": form})

def traitement (request):
    cform = ContinentForm(request.POST)
    if cform.is_valid():
        continent = cform.save()
        return HttpResponseRedirect("/paysapp/")
    else :
        return render (request, "continent/ajout.html", {"form": cform})

def index(request):
    liste =list(models.Continent.objects.all())
    return render(request, "continent/index.html", {"liste": liste})

def affiche(request, id):
    continent = models.Continent.objects.get(pk=id)
    liste=models.Pays.objects.filter(continent_id=id)
    return render(request, "continent/affiche.html",{"continent": continent,"liste": liste})

def update (request, id):
    continent = models.Continent.objects.get(pk=id)
    form = ContinentForm(continent.dico())
    return render(request, "continent/update.html",{"form":form, "id": id})

def updatetraitement (request, id):
    cform = ContinentForm(request.POST)
    if cform.is_valid():
        continent = cform.save(commit = False)
        continent.id = id
        continent.save()
        return HttpResponseRedirect("/paysapp/")
    else:
        return render(request, "continent/ajout.html", {"form": cform, "id": id})

def delete (request, id):
    continent = models.Continent.objects.get(pk=id)
    continent.delete()
    return HttpResponseRedirect("/paysapp/")