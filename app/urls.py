from django.urls import path
from . import views
from .views import ArticleListView
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView, 
   ArticleCreateView, 


    RecipeListView,
    RecipeUpdateView,
    RecipeDetailView,
    RecipeDeleteView, 
    RecipeCreateView, 
)

urlpatterns = [

    path('', views.index, name='index'),
    path('config/', views.stripe_config),#new
    path('create-checkout-session/', views.create_checkout_session),#latest
    path('success/', views.success),  # new
    path('cancel/', views.cancel),  # new
    path('webhook/', views.stripe_webhook),  # new


    path('<int:pk>/edit/',ArticleUpdateView.as_view(), name='article_edit'), 
    path('<int:pk>/',ArticleDetailView.as_view(), name='article_detail'), 
    path('<int:pk>/delete/',ArticleDeleteView.as_view(), name='article_delete'),  
    path('article/', ArticleListView.as_view(), name='article_list'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),


    path('<int:pk>/edit/recipe/',RecipeUpdateView.as_view(), name='recipe_edit'), 
    path('<int:pk>/recipe/',RecipeDetailView.as_view(), name='recipe_detail'), 
    path('<int:pk>/delete/recipe/',RecipeDeleteView.as_view(), name='recipe_delete'),  
    path('recipe/', RecipeListView.as_view(), name='recipe_list'),
    path('new/recipe/', RecipeCreateView.as_view(), name='recipe_new'),
]