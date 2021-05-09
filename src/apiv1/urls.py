from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DrinkViewSet

app_name = 'apiv1'

router = DefaultRouter()

router.register(r'drinks', DrinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
