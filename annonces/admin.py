from django.contrib import admin
from .models import Annonce,Categorie

# Register your models here.
#ici, nous indiquons à Django de prendre en compte les modèles Annonce et categorie
admin.site.register(Categorie)
admin.site.register(Annonce)