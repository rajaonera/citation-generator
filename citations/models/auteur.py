from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
