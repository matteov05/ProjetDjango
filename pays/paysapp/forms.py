from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class PaysForm(ModelForm):
    class Meta :
        model = models.Pays
        fields = ('nom', 'date_visite', 'note', 'avis')
        labels = {
            'nom': _('Nom du pays'),
            'date_visite': _('Date de Visite'),
            'note': _('Note'),
            'avis': _('Avis')
        }

class ContinentForm(ModelForm):
    class Meta :
        model = models.Continent
        fields = ('nom', 'description')
        labels = {
            'nom': _('Nom du Continent'),
            'description': _('Description'),
        }