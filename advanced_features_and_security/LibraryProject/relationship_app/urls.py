from django.urls import path
from . import views

urlpatterns = [
    # Book management
    path('books/', views.list_books, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

    # Authentication
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),

    # Role-based views
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
