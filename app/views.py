from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import RecipeForm
from .models import Recipe
from .utils import save_image


def home(request):
    recipes = Recipe.objects.all()[:5]
    return render(request, 'home.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_update.html'
    success_url = '/'
    pk_url_kwarg = 'recipe_id'

    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        
        if 'image' in self.request.FILES:
            uploaded_image = self.request.FILES['image']
            saved_filename = save_image(uploaded_image)
            form.instance.image = f'{saved_filename}'
        
        return super().form_valid(form)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_create.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'recipe_id'
    
    def form_valid(self, form):
        form.instance.author = self.request.user

        if 'image' in self.request.FILES:
            uploaded_image = self.request.FILES['image']
            saved_filename = save_image(uploaded_image)
            form.instance.image = f'{saved_filename}'
        
        return super().form_valid(form)
    

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'recipe_id'

    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user