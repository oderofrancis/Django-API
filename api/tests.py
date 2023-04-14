from django.test import TestCase
from django.urls import reverse
from .models import *

# Create your tests here.

class BookTests(TestCase):
    @classmethod

    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Harry Potter",
            subtitle = "The Philosopher's Stone",
            author = "J.K. Rowling",
            isbn = "9780747532743"
        )
    
    def test_book_content(self):
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.subtitle}", "The Philosopher's Stone")
        self.assertEqual(f"{self.book.author}", "J.K. Rowling")
        self.assertEqual(f"{self.book.isbn}", "9780747532743")

    def test_book_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'api/book_list.html')