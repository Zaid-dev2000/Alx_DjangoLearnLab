from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden, HttpResponse
from .models import Book

@permission_required('app_name.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

@permission_required('app_name.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return HttpResponse("Book created successfully")
    return render(request, 'books/create_book.html')

@permission_required('app_name.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return HttpResponse("Book updated successfully")
    return render(request, 'books/edit_book.html', {'book': book})

@permission_required('app_name.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return HttpResponse("Book deleted successfully")


def example_view(request):
    if request.method == 'POST':
        # Process form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        # Perform operations with the submitted data
        return render(request, 'success.html')
    return render(request, 'example_form.html')  # Render the form