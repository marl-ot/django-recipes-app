from django.contrib.auth.models import User
from recipe_site import settings
from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preparation_steps = models.TextField()
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to=f'{settings.MEDIA_URL[1:]}')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class RecipeCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RecipeCategoryRelation(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recipe} ({self.category})"