from django import forms
from .models import Citation,Auteur,Theme,Commentaire

class CitationForm(forms.ModelForm):
    class Meta:
        model = Citation
        fields = ['auteur', 'theme', 'citation']
        widgets = {
            'citation': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded',
                'rows': 3,
                'placeholder': 'Tapez votre citation ici...'
            }),
            'auteur': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'theme': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
        }

class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = ['nom']
        widgets = {
            'nom': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded',
                'rows': 3,
                'placeholder': 'Tapez votre nom ici...'
            }),
        }

class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name']
        widgets = {
            'name': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded',
                'rows': 3,
                'placeholder': 'Tapez votre theme ici...'
            }),
        }

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenue']
        widgets = {
            'contenue': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded',
                'rows': 3,
                'placeholder': 'Tapez votre commentaire ici...'
            }),
        }