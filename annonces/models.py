from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=30,null=True)

    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.nom


class Annonce(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    photo = models.ImageField(default='default.png', blank=True)
    publiee = models.BooleanField(default=False)
    prix = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.titre

    def _get_unique_slug(self):
        slug = slugify(self.titre)
        unique_slug = slug
        num = 1
        while Annonce.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save() # Call the real save() method(self, *args, **kwargs):
        

    @classmethod
    def publiees(cls):
        return cls.objects.filter(publiee=True).order_by('prix')

    @classmethod
    def liste_publiees(cls,catId):
        return cls.publiees().filter(categorie_id=catId)

    @classmethod
    def search(cls,query):
        if query == '':
            return []
        else:
            return cls.publiees().filter(titre__contains=query)

# class Livre(models.Model):
#     nom= models.CharField(max_length=100)

#     def __str__(self):
#         return self.nom 

    
# class Ecrivain(models.Model):
#     nom = models.CharField(max_length=100)
#     prenom = models.CharField(max_length=100)
#     email = models.EmailField(max_length = 100)
#     Livre =  models.ForeignKey(Livre, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.nom






