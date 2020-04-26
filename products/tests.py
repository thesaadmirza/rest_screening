from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product


class AccountTests(APITestCase):
    url = reverse('products-list')

    def test_create_product(self):
        """
        Ensure we can create a new product object.
        """

        data = {'title': 'Mobile', 'description': 'here is description'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().title, 'Mobile')

    def test_get_product(self):
        """
        Ensure we can product after creating it.
        :return:
        """
        self.test_create_product()
        response = self.client.get('/products/1/')
        self.assertEqual(response.data, {'title': 'Mobile', 'description': 'here is description'})
