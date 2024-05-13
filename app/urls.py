from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import RecipeCreateView, RecipeUpdateView, RecipeDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/update/', RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe/<int:recipe_id>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('recipe/create/', RecipeCreateView.as_view(), name='recipe_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
