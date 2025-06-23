import random
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CitationForm,ThemeForm,AuteurForm,CommentaireForm
from .models import Citation, Commentaire

def citation_aleatoire(request):
    citation = Citation.objects.order_by('?').first()
    commentaires = Commentaire.objects.filter(citation=citation)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "Vous devez être connecté pour commenter.")
            return redirect('login')  # ou vers la même page

        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.citation = citation
            commentaire.user = request.user
            commentaire.save()
            return redirect('citation_aleatoire')  # éviter re-post en F5
    else:
        form = CommentaireForm()

    return render(request, 'citations/aleatoire.html', {
        'citation': citation,
        'form': form,
        'commentaires': commentaires
    })

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

def ajouter_commentaire(request):
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citation_aleatoire')  # ou une page de confirmation
    else:
        form = CommentaireForm()

    return render(request, 'citations/ajouter_commentaire.html', {'form': form})
