from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from datetime import datetime
from .models import Annonce,Categorie
from .forms import AnnonceForm
# Create your views here.
def categorie_annonce(request,catId):
    _annonces = Annonce.liste_publiees(catId)
    context = {
        'categorie':Categorie.objects.get(id=catId),
        'annonce':_annonces,
        'annonce_count' :len(_annonces)
    }
    return render(request,'annonces/showCategorie.html',context)


def home(request):
    """ c'est une exemple de page mais qui respecte pas les normes """
    context = {
        'annonce': Annonce.objects.order_by('prix'),   
        'categorie':Categorie.objects.all()
    }
    return render(request,'annonces/home.html',context)

def search(request):
    query = request.GET.get('query','')
    context={
        'annonce':Annonce.search(query)
    }
    return render(request,'annonces/resultat.html',context)

def show_annonce(request,id):
        context= {
            'annonce':Annonce.objects.get(id=id)
        }
        return render(request,'annonces/showAnnonces.html',context)

def view_article(request,id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    if id_article > 100:
        raise Http404
    
    return redirect(view_redirection)

    # return HttpResponse(
    #     "VOUS AVEZ DEMANDE l'article #{0}".format(id_article)
    # )


def index(request):
    context = {
        'annonce':Annonce.objects.all(),
        'categorie':Categorie.objects.all()
    }
    return render(request,'annonces/index.html',context)

def addAnnonce(request):
    formulaire = AnnonceForm()
    context = {
        'formulaire':formulaire
    }
    if request.method=='POST':
        formulaire = AnnonceForm(request.POST,request.FILES)
        if formulaire.is_valid():
            annonce = Annonce(**formulaire.cleaned_data)
            annonce.save()
            return redirect('afficher_annonce',id=annonce.id)
    else:
        return render(request,'annonces/formulaire.html',context)

def annonce(request,id):
    """
    affiche l'annonce en fonction de l'id
    """
    context = {
        'annonce' : Annonce.objects.get(id=id)
    }
    return render(request,'annonces/annonce.html',context)

def view_redirection(request):
    return HttpResponse(
        "Vous avez ete redirige ici"
    ) 


def afficheTemplate(request):
    """ 
    La fonction render  est en réalité une méthode de django.shortcut  qui nous
    simplifie la vie : elle génère un objet HttpResponse  après avoir traité notre template.
    la fonction render prend en argument trois paramètres :
    1.La requête HTTP initiale, que l'on appelle request  par convention pour rappel ;
    2.Le chemin vers le template adéquat dans un des dossiers de templates donnés dans settings.py;
    3.Un dictionnaire reprenant les variables qui seront accessibles dans le template.
    """
    return render(request,'annonces/affiche.html',{'date':datetime.now()})
    