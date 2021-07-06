from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        'all_books': Book.objects.all(),
        'all_authors': Author.objects.all()
    }
    return render(request, 'books_authors.html', context)

def add_book(request):
    Book.objects.create(
        title=request.POST['book_title'],
        desc=request.POST['book_desc']
    )

    return redirect('/')

def book_details(request, number):
    if request.method=='GET':
        this_book = Book.objects.get(id=number)
        return redirect(f'/results/{this_book.id}')
    
    if request.method=='POST':
        this_book = Book.objects.get(id=number)
        this_author = request.POST['author']
        add_author = this_book.authors.add(this_author)
        return redirect(f'/results/{this_book.id}')

def results(request, number):
    context = {
            'this_book' : Book.objects.get(id=number),
            'this_author': Author.objects.get(id=number),
            'all_books': Book.objects.all(),
            'all_authors': Author.objects.all()
        }
    return render(request, 'book_details.html', context)

# ADD AUTHOR PAGES

def authors(request):
    context = {
        'all_books': Book.objects.all(),
        'all_authors': Author.objects.all()
    }
    return render(request, 'authors_books.html', context)

def add_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'], 
        last_name=request.POST['last_name'], 
        notes=request.POST['notes']
        )
    return redirect('/authors')

def author_details(request, number):
    if request.method=='GET':
        this_author = Author.objects.get(id=number)
        return redirect(f'/author-results/{this_author.id}')
    if request.method=='POST':
        this_book = request.POST['book']
        this_author=Author.objects.get(id=number)
        add_book=this_author.books.add(this_book)
        return redirect(f'/author-results/{this_author.id}')


def author_results(request, number):
    context = {
        'all_books': Book.objects.all(),
        'all_authors': Author.objects.all(),
        'this_author': Author.objects.get(id=number),
    }
    return render(request, 'authors_details.html', context)


