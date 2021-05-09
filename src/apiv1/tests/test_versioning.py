"""Tests for api versioning """

from src.apiv1.tests.base import BaseTestCase


class TestRequestVersion(BaseTestCase):
    """ Test version settings"""

    def test_unversioned_request(self):
        """Test the output of the view for getting unversioned request"""
        response = self.client.get('/api/drinks/')
        self.assertEqual(200, response.status_code)

    def test_query_param_versioning(self):
        response = self.client.get('/api/drinks/?version=v1')
        self.assertEqual(200, response.status_code)
    
    def test_invalid_query_param_versioning(self):
        response = self.client.get('/api/drinks/?version=v2')
        self.assertEqual(404, response.status_code)
        self.assertEqual(
            "Invalid version in query parameter.",
            response.data['detail'])
