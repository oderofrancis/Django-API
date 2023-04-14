from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import *

# Create your tests here.

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Harry Potter",
            subtitle = "The Philosopher's Stone",
            author = "J.K. Rowling",
            isbn = "9780747532743"
        )
    
    def test_api_content(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(),1)
        response.data[0]