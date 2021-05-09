"""Tests for drinks api """

from rest_framework import status

from src.apiv1.tests.base import BaseTestCase


class TestDrinksAPI(BaseTestCase):
    """ Test drinks CRUD"""

    def test_create_custom_drink(self):
        response = self.client.post('/api/drinks/', self.drink_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_one_custom_drink(self):
        drink_id = self.new_drink.id
        response = self.client.get('/api/drinks/{}/'.format(drink_id))
        self.assertEqual(200, response.status_code)
    
    def test_patch_one_custom_drink(self):
        drink_id = self.new_drink.id
        response = self.client.patch(
            '/api/drinks/{}/'.format(drink_id), self.drink_data_patch, format="json")
        self.assertEqual(200, response.status_code)

    def test_put_one_custom_drink(self):
        drink_id = self.new_drink.id
        response = self.client.put(
            '/api/drinks/{}/'.format(drink_id), self.drink_data_put, format="json")
        self.assertEqual(200, response.status_code)

    def test_delete_one_custom_drink(self):
        drink_id = self.new_drink.id
        response = self.client.delete('/api/drinks/{}/'.format(drink_id))
        self.assertEqual(204, response.status_code)
