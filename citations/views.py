import random
from django.shortcuts import render
from .models import Citation
from .forms import CitationForm,ThemeForm,AuteurForm

def citation_aleatoire(request):
    citations = Citation.objects.all()
    citation = random.choice(citations) if citations else None
    return render(request, 'citations/aleatoire.html', {'citation': citation})

def ajouter_citation(request):
    if request.method == 'POST':
        form = CitationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citation_aleatoire')  # ou une page de confirmation
    else:
        form = CitationForm()

    return render(request, 'citations/ajouter_citation.html', {'form': form})

def ajouter_theme(request):
    if request.method == 'POST':
        form = ThemeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citation_aleatoire')  # ou une page de confirmation
    else:
        form = ThemeForm()

    return render(request, 'citations/ajouter_theme.html', {'form': form})

def ajouter_auteur(request):
    if request.method == 'POST':
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citation_aleatoire')  # ou une page de confirmation
    else:
        form = AuteurForm()

    return render(request, 'citations/ajouter_auteur.html', {'form': form})
