from django import forms
from .models import Annonce

class AnnonceForm(forms.ModelForm):
    """Form definition for Annonce."""

    class Meta:
        """Meta definition for Annonceform."""

        model = Annonce
        fields = ('titre','auteur','photo','publiee','contenu','prix','categorie')
