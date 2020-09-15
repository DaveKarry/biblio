from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Genre, Author
from .forms import Book_form, Author_form, Genre_form
from django.shortcuts import redirect


# Create your views here.
def book_list(request):
    books = Book.objects.order_by('title')
    return render(request, 'biblio/books_list.html', {'books': books})

def genre_list(request):
    genres = Genre.objects.order_by('name')
    return render(request, 'biblio/genres_list.html', {'genres': genres})

def author_list(request):
    authors = Author.objects.order_by('first_name')
    return render(request, 'biblio/authors_list.html', {'authors': authors})



def book_new(request):
    if request.method == "POST":
        form = Book_form(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_list')
    else:
        form = Book_form()
        return render(request, 'biblio/books_edit.html',{'form': form})

def genre_new(request):
    if request.method == "POST":
        form = Genre_form(request.POST)
        if form.is_valid():
            genre = form.save(commit=False)
            genre.save()
            return redirect('genre_list')
    else:
        form = Genre_form()
        return render(request, 'biblio/genres_edit.html',{'form': form})

def author_new(request):
    if request.method == "POST":
        form = Author_form(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('author_list')
    else:
        form = Author_form()
        return render(request, 'biblio/authors_edit.html',{'form': form})
