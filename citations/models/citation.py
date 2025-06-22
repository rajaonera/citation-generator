from django.db import models
from .auteur import Auteur
from .theme import Theme

class Citation(models.Model):
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    citation = models.TextField()

    def __str__(self):
        return f'"{self.citation}" - {self.auteur.nom}'
