from django.shortcuts import render, redirect
from .models import Book
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from author.models import Author
from order.models import Order
from authentication.models import CustomUser


def book_index(request):
    return render(request, 'books.html')


def get_book_list(request):
    if request.method == "GET":
        return render(request, 'book_list.html', {"books": Book.get_all()})


def create_book(request):
    aut_list = []
    if request.method == "GET":
        return render(request, 'create_book.html')
    if request.method == "POST":
        book = Book()
        name = request.POST['name']
        description = request.POST['description']
        count = request.POST['count']
        authors = request.POST['authors']
        book = book.create(name=name, description=description, count=count)
        if authors:
            authors = authors.split(",")
            for author in authors:
                auth = Author()
                auth = auth.get_by_id(int(author))
                if auth is not None:
                    aut_list.append(auth)
            book.add_authors(aut_list)

        return redirect('book')


def get_book_info(request, id):
    if request.method == 'GET':
        book = Book.get_by_id(id)
        return render(request, 'book_info.html', {'book': book})
    if request.method == "POST":
        book = Book()
        if book.get_by_id(id):
            book.delete_by_id(id)
            return redirect('book')
    else:
        return render(request, 'book_list.html')


def book_update(request, id):
    book = Book.get_by_id(id)

    if request.method == "GET":
        return render(request, 'book_update.html', {'book': book})
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        count = request.POST["count"]
        authors = request.POST["author"]
        author_delete = request.POST["author_delete"]
        if authors:
            aut_list = []
            authors = authors.split(",")
            for author in authors:
                auth = Author()
                auth = auth.get_by_id(int(author))
                if auth is not None:
                    aut_list.append(auth)
            book.add_authors(aut_list)
        if author_delete:
            aut_list = []
            author_delete = author_delete.split(",")
            for author in author_delete:
                auth = Author()
                auth = auth.get_by_id(int(author))
                if auth is not None:
                    aut_list.append(auth)
            book.remove_authors(aut_list)
        book.update(name=name, description=description, count=count)
        return redirect('get_book_info', id=id)


def get_book_list(request):
    search_term = request.GET.get('searchTerm', '')
    books = Book.objects.all()

    if search_term:
        books = books.filter(Q(name__icontains=search_term) |
                             Q(description__icontains=search_term) |
                             Q(authors__name__icontains=search_term))

    context = {
        'books': books
    }

    return render(request, 'book_list.html', context)


def delete_book(request, id):
    if request.method == "POST":
        book = Book()
        if book.get_by_id(id):
            book.delete_by_id(id)
            return redirect('book')
    else:
        return render(request, 'book_list.html')


def get_certain_user_order(request, id):
    if request.method == "GET":
        auth_lst = []
        author_names = []
        user = CustomUser()
        user = user.get_by_id(id)
        orders = Order.objects.filter(user=user)
        for order in orders:
            for auth in Author.objects.filter(books=order.book):
                auth_books = auth.books.all()
                for book in auth_books:
                    if book.id == order.book.id:
                        auth_lst.append(book)

        for book in auth_lst:
            print(book)
            authors = book.authors.all()
            for author in authors:
                author_names.append(author.name)
        print(author_names)
        return render(request, "book_list2.html", {"orders": orders, "orders_len": len(orders),"authors": author_names})

    return render(request, "book_list2.html")

def get_id(request):
    if request.method == "POST":
        id = int(request.POST["id"])
        return redirect('get_certain_user_order', id)
    return render(request, "get_id.html")
