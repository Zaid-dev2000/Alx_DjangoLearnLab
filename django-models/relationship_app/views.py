from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library  # Import the models

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # Specify the model to use for this view
    template_name = 'relationship_app/library_detail.html'  # Use the specified template
    context_object_name = 'library'  # Name of the object in the template context


