from rest_framework import viewsets, status
from rest_framework.response import Response


from src.apiv1.models.drinks import Drink
from src.apiv1.serializers.drinks import DrinkReadSerializer, DrinkModelSerializer


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
