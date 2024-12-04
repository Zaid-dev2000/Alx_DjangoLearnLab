from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
from django.contrib.auth.models import User



class BookAPITests(APITestCase):
    def setUp(self):
        """
        Create initial test data and authenticate the test client.
        """
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)  # Authenticate the client
        self.list_url = reverse('book-list')  # URL for the list endpoint
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.id})  # URL for the detail endpoint

    def test_list_books(self):
        """
        Ensure the list endpoint returns all books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure one book is returned
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_retrieve_book(self):
        """
        Ensure the detail endpoint retrieves the correct book.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_create_book(self):
        """
        Ensure a new book can be created.
        """
        data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 1998,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Ensure the book is created

    def test_update_book(self):
        """
        Ensure an existing book can be updated.
        """
        data = {
            "title": "Harry Potter and the Sorcerer's Stone",
            "publication_year": 1997,
            "author": self.author.id
        }
        self.client.force_authenticate(user=self.user)  # Authenticate the client
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter and the Sorcerer's Stone")

    def test_delete_book(self):
        """
        Ensure a book can be deleted.
        """
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Ensure the book is deleted

    def test_filter_books_by_title(self):
        """
        Ensure filtering by title works.
        """
        response = self.client.get(f"{self.list_url}?title={self.book.title}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """
        Ensure searching by title or author works.
        """
        response = self.client.get(f"{self.list_url}?search=Harry")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        """
        Ensure ordering by publication year works.
        """
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_access(self):
        """
        Ensure unauthenticated users have read-only access.
        """
        self.client.logout()  # Ensure the client is unauthenticated
        response = self.client.post(self.list_url, {"title": "New Book",
        "publication_year": 2020,
        "author": self.author.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
