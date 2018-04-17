from django.db import models

# Create your models here.

class Editeur(models.Model):
    id_editeur = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=45)
    
class Commande(models.Model):
    num_commande = models.CharField(max_length=20,primary_key=True)
    demandeur = models.CharField(max_length=45)
    auteur = models.TextField()
    titre = models.TextField()
    editeur = models.CharField(max_length=45)
    commentaire = models.TextField()
    prix = models.IntegerField()
    etat = models.CharField(max_length=20)
    ISBN = models.CharField(max_length=20)
    fournisseur = models.CharField(max_length=30)
    
class Auteur(models.Model):
    id_auteur = models.IntegerField(primary_key=True)
    nom = models.TextField()
    prenom = models.TextField()

class Livre_abstrait(models.Model):
    id_livre_abstrait = models.IntegerField(primary_key=True)
    ISBN = models.CharField(max_length=20)
    titre_livre = models.TextField()
    num_collection = models.CharField(max_length=20)
    AMS = models.IntegerField()
    Mots_cles = models.TextField()
    Langue = models.CharField(max_length=20)
    Langue_originale = models.CharField(max_length=20)
    date = models.DateField()
    auteur = models.ForeignKey(Auteur,on_delete= models.SET_DEFAULT,default='')
    editeur=models.ForeignKey(Editeur,on_delete= models.SET_DEFAULT,default='')


class Livre(models.Model): 
    Numero_inventaire = models.IntegerField(primary_key=True)
    Côte= models.CharField(max_length=45)
    Perdu=models.BooleanField()
    Commande=models.ForeignKey(Commande,on_delete= models.SET_DEFAULT,default='')
    Livre_abstrait=models.ForeignKey(Livre_abstrait,on_delete= models.SET_DEFAULT,default='')



class Emprunteurs(models.Model):
    id_emprunteur = models.IntegerField(primary_key=True)
    nom = models.TextField()
    divers = models.TextField()
    Livre_abstrait=models.ForeignKey(Livre_abstrait,on_delete= models.SET_DEFAULT,default='')


class Emprunts(models.Model):
    id_emprunts = models.IntegerField(primary_key=True)
    date = models.DateField()
    emprunteurs = models.ForeignKey(Emprunteurs,on_delete= models.SET_DEFAULT,default='')

