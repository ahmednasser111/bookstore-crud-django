from django.shortcuts import render, redirect
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})
def create(request):

    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price=request.POST['price']
        )
        return redirect('/')
    return render(request, 'books/create.html')
def edit(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.save()
        return redirect('/')
    return render(request, 'books/edit.html', {'book': book})
def delete(request, id):
    book = Book.objects.get(id=id)

    book.delete()
    return redirect('/')
def show(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'books/show.html', {'book': book})
