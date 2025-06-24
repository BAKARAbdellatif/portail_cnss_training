from django.db import models


# Create your models here.
class Assure(models.Model):
    nom = models.CharField(max_length=255)
    numero_cnss = models.CharField(unique=True, max_length=255)
    date_naissance = models.DateField()
    adresse = models.TextField()

    def __str__(self):
        return f"Nom : {self.nom} - Numero CNSS : {self.numero_cnss}"
