from django.contrib import admin
from .models import Recipe, RecipeCategory, RecipeCategoryRelation


admin.site.register(Recipe)
admin.site.register(RecipeCategory)
admin.site.register(RecipeCategoryRelation)