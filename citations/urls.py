from django.urls import path
from .views import citation_aleatoire

urlpatterns = [
    path('', citation_aleatoire, name='citation_aleatoire'),
]
