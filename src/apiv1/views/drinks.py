from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apiv1.models.drinks import Drink
from src.apiv1.serializers.drinks import DrinkReadSerializer, DrinkModelSerializer
from src.apiv1.utils.cocktails import get_five_random_cocktails, get_cocktails_details


class DrinkViewSet(viewsets.ModelViewSet):
    """ Custom drink(s) view endpoint"""

    queryset = Drink.objects.all()
    serializer_class = DrinkReadSerializer

    def update(self, request, *args, **kwargs):
        """ Custom drink update endpoint"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = DrinkModelSerializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """ Custom drink creation endpoint"""
        serializer = DrinkModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ListRandomCocktails(APIView):
    """
    View to list five random cocktails.
    """
    def get(self, request, format=None):
        """
        Return a list of five random cocktails.
        """
        cocktails = get_five_random_cocktails()
        res = {"drinks": cocktails}
        return Response(res)


class ViewCocktailDetails(APIView):
    """
    View to for a cocktail details
    """

    def get(self, request, id=None, format=None):
        """
        Return a cocktail detail.
        """
        cocktail = get_cocktails_details(id)
        if not cocktail:
            data = {"msg": "ID provided was not Found."}
            return Response(data)
        return Response(cocktail)
