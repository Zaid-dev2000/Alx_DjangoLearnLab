from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(ListCreateAPIView):
    """
    Handles listing all books and creating a new book.
    Permissions:
        - Unauthenticated users: Read-only access (GET).
        - Authenticated users: Full access (GET, POST).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Customize the creation logic.
        """
        serializer.save()  # Add custom logic here if needed
        # Example: Notify admin about the new book (future enhancement)


class BookDetailView(RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, or deleting a specific book by ID.
    Permissions:
        - Unauthenticated users: Read-only access (GET).
        - Authenticated users: Full access (GET, PUT, PATCH, DELETE).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        """
        Customize the update logic.
        """
        serializer.save()  # Add custom update logic if needed
        # Example: Log updates for analytics (future enhancement)

