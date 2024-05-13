from django.shortcuts import render, HttpResponseRedirect
from .forms import PaysForm
from .import models

# Create your views here.
def ajout (request,id):
    if request.method == "POST":
        form = PaysForm(request)
        return render(request, "pays/ajout.html", {"form": form,"id": id})
    else :
        form = PaysForm()
        return render(request, "pays/ajout.html", {"form": form,"id": id})

def traitement (request, id):
    continent = models.Continent.objects.get(pk=id)
    pform = PaysForm(request.POST)
    if pform.is_valid():
        pays = pform.save(commit=False)
        pays.continent = continent
        pays.continent_id = id
        pays.save()
        return HttpResponseRedirect("/paysapp/index/")
    else :
        return render(request, "pays/ajout.html", {"form": pform})

def index(request):
    liste =list(models.Pays.objects.all())
    return render(request, "pays/index.html", {"liste": liste})

def affiche(request, id):
    pays = models.Pays.objects.get(pk=id)
    return render(request, "pays/affiche.html",{"pays": pays})

def update (request, id):
    pays = models.Pays.objects.get(pk=id)
    form = PaysForm(pays.dico())
    return render(request, "pays/update.html",{"form":form, "id": id})

def updatetraitement (request, id):
    pform = PaysForm(request.POST)
    if pform.is_valid():
        pays = pform.save(commit = False)
        pays.id = id
        pays.save()
        return HttpResponseRedirect("/paysapp/index/")
    else:
        return render(request, "pays/ajout.html", {"form": pform, "id": id})


def delete (request, id):
    pays = models.Pays.objects.get(pk=id)
    pays.delete()
    return HttpResponseRedirect("/paysapp/index/")



