from django.db import models
from . import Citation
from django.contrib.auth.models import User

class Commentaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    citation = models.ForeignKey(Citation, on_delete=models.CASCADE)
    contenue = models.TextField()

    def __str__(self):
        return f'"{self.citation.citation}" - {self.user.email} - {self.contenue}'
@property
def auteur_nom(self):
    return self.user.username if self.user else "Anonyme"
