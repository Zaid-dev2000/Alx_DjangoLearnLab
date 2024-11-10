from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view
]
from django.urls import include, path

urlpatterns = [
    path('relationship_app/', include('relationship_app.urls')),
]
