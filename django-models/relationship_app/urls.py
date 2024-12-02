from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

# Consolidated urlpatterns
urlpatterns = [
    # URLs for authentication
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),  # Optional: Home view for authenticated users

    # URLs for book management
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('books/', views.list_books, name='list_books'),  # Function-based view for listing books

    # Class-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # URLs for user roles
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # Including additional apps
    path('relationship_app/', include('relationship_app.urls')),
]
