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

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Optional: A home view to redirect to after login/registration
@login_required
def home(request):
    return render(request, 'relationship_app/home.html')

