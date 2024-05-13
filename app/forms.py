from django import forms
from .models import Recipe
from django.utils.translation import gettext_lazy as _


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_steps', 'preparation_time', 'image']
        labels = {
            'title': _('Название'),
            'description': _('Описание'),
            'preparation_steps': _('Шаги приготовления'),
            'preparation_time': _('Время приготовления'),
            'image': _('Изображение'),
        }