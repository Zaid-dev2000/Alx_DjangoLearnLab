from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


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
