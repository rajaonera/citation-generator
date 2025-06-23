from django.urls import path
from .views import citation_aleatoire, ajouter_citation, ajouter_theme, ajouter_auteur

urlpatterns = [
    path('', citation_aleatoire, name='citation_aleatoire'),
    path('ajouter/citation', ajouter_citation, name='ajouter_citation'),
    path('ajouter/theme', ajouter_theme, name='ajouter_theme'),
    path('ajouter/auteur', ajouter_auteur, name='ajouter_auteur'),
    path('login', login, name='login'),
]
