import random
from django.shortcuts import render
from .models import Citation

def citation_aleatoire(request):
    citations = Citation.objects.all()
    citation = random.choice(citations) if citations else None
    return render(request, 'citations/aleatoire.html', {'citation': citation})
