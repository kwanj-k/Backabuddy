from rest_framework import serializers

from src.apiv1.models.drinks import Drink


class DrinkModelSerializer(serializers.ModelSerializer):
    """ Drinks model serializer for writes"""

    class Meta:
        model = Drink
        exclude = ('deleted',)


class DrinkReadSerializer(serializers.Serializer):
    """ Drinks bare serializer for reads"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    category = serializers.CharField(read_only=True)
    image = serializers.URLField(read_only=True)
    is_alcoholic = serializers.BooleanField(read_only=True)
    instructions = serializers.CharField(read_only=True)
    ingredients = serializers.ListField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
