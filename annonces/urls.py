from django.urls import path, re_path
from . import views



urlpatterns = [
    path('',views.home),
    #re_path(r'^article/(?P<id_article>.+)', views.view_article), methode regex
    path('article/<int:id_article>', views.view_article,name='afficher_article'), 
    path('redirection',views.view_redirection),
    path('search',views.search,name="search"),
    path('annonce/new',views.addAnnonce,name='addAnnonce'),
    path('annonces/<int:id>',views.show_annonce,name="afficher_annonce"),
    path('categories/<int:catId>/annonces',views.categorie_annonce,name="afficher_categorie"),
    path('affiche',views.afficheTemplate), 
    path('annonce/<int:id>',views.annonce),
    path('index',views.index),
]