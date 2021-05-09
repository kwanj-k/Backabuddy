from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DrinkViewSet, ListRandomCocktails, ViewCocktailDetails

app_name = 'apiv1'

router = DefaultRouter()

router.register(r'drinks', DrinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('random_cocktails', ListRandomCocktails.as_view(), name='cocktails'),
    path('cocktail_details/<int:id>',
         ViewCocktailDetails.as_view(), name='cocktail_details'),
]
