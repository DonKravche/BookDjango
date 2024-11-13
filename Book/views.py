from django.shortcuts import render, redirect

from .forms import BookForm
from .models import Book, Category


# Create your views here.

def index(request):
    book_title = request.GET.get('book_title')
    selected_categories = request.GET.getlist('category')

    books = Book.objects.all()

    if book_title:
        books = books.filter(title__icontains=book_title)

    if selected_categories:
        books = books.filter(category__id__in=selected_categories)

    categories = Category.objects.all()
    categories_by_type = {}

    for category in categories:
        category_type = category.category_type
        if category_type not in categories_by_type:
            categories_by_type[category_type] = []
        categories_by_type[category_type].append(category)

    return render(request, 'index.html', {
        'books': books,
        'categories_by_type': categories_by_type
    })


def addBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('Book:index')
        else:
            return render(request, 'book_add.html', {'form': form})
    else:
        form = BookForm()
        return render(request, 'book_add.html', {'form': form})
