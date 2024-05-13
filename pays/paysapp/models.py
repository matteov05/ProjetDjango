from django.db import models

# Create your models here.

class Pays(models.Model):
    nom = models.CharField(max_length=100)
    date_visite = models.DateField(blank = True, null= True)
    note = models.IntegerField(blank=False)
    avis = models.TextField(null = True, blank = True)
    continent= models.ForeignKey("continent", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"Vous avez visité le pays {self.nom} et vous avez mis la note de {self.note}"
        return chaine

    def dico(self):
        return {"nom":self.nom, "date_visite":self.date_visite, "note":self.note, "avis":self.avis, "continent":self.continent}


class Continent(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.nom

    def dico(self):
        return {"nom":self.nom, "description":self.description}