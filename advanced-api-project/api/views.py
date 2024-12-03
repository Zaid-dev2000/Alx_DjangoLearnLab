from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from rest_framework import generics



class BookListView(ListAPIView):
    """
    Handles listing all books.
    Permissions:
        - Unauthenticated users: Read-only access (GET).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(RetrieveAPIView):
    """
    Handles retrieving a specific book by ID.
    Permissions:
        - Unauthenticated users: Read-only access (GET).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(CreateAPIView):
    """
    Handles creating a new book.
    Permissions:
        - Authenticated users only (POST).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookUpdateView(UpdateAPIView):
    """
    Handles updating an existing book.
    Permissions:
        - Authenticated users only (PUT, PATCH).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDeleteView(DestroyAPIView):
    """
    Handles deleting a book.
    Permissions:
        - Authenticated users only (DELETE).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookListView(ListCreateAPIView):
    """
    List all books with filtering, searching, and ordering capabilities.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']  # Fields for searching
    ordering_fields = ['title', 'publication_year']  # Fields for ordering
    ordering = ['title']  # Default ordering

    """
Filtering, searching, and ordering features:
- Filtering: Use query parameters (e.g., ?title=Harry) to filter results.
- Searching: Use the 'search' query parameter to search books by title or author name.
- Ordering: Use the 'ordering' query parameter to sort results (e.g., ?ordering=title or ?ordering=-publication_year).
"""
