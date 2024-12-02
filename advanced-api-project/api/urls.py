from django.urls import path
from .views import BookListView, BookDetailView
from django.urls import path, include

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include API app URLs
]
