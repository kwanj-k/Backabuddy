"""Common functionality in testing."""

from rest_framework.test import APITestCase, APIClient

from src.apiv1.models import Drink


class BaseTestCase(APITestCase):
    """Base testing class."""

    def setUp(self):
        """Initialize testing database."""
        self.client = APIClient()
        self.drink_data = {
            "name": "Orange Juice",
            "category": "Fruit Juice",
            "is_alcoholic": False,
            "instructions": 'How to make',
            "ingredients": ['sugar', 'water'],
        }
        self.drink_data_2 = {
            "name": "Orange Juice 2",
            "category": "Fruit Juice 2",
            "is_alcoholic": False,
            "instructions": 'How to make',
            "ingredients": ['sugar', 'water'],
        }
        self.drink_data_patch = {
            "ingredients": ['sugar', 'water', 'oranges'],
        }
        self.drink_data_put = {
            "name": "Orange Juice",
            "category": "Fruit Juice",
            "is_alcoholic": False,
            "instructions": 'How to make the juice',
            "ingredients": ['sugar', 'water', 'lemon'],
        }
        self.new_drink = Drink.objects.create(**self.drink_data_2)
