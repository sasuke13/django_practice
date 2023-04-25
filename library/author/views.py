from django.shortcuts import render, redirect
from .models import Author
from django.contrib import messages
from django.shortcuts import get_object_or_404


def main_form(request):
    return render(request, "author/author.html")


def get_all(request):
    return render(request, "author/author.html", {"text": Author.get_all()})


def create_author(request):
    if request.method == "POST":
        auth = Author()
        name = request.POST["name"]
        surname = request.POST["surname"]
        patronymic = request.POST["patronymic"]

        auth.create(name=name, surname=surname, patronymic=patronymic)
        messages.success(request, "Author was created successfully!")
        return redirect('get_all_authors')
    else:
        return render(request, 'author/author.html')


def delete_author(request):
    if request.method == "POST":
        id = int(request.POST["id"])
        auth = get_object_or_404(Author, id=id)

        if not auth.books.exists():
            auth.delete()
            messages.success(request, "Author was deleted successfully!")
            return redirect('get_all_authors')
        else:
            messages.success(request, "You wrote an id of author, which is bounded to certain book!")
            return render(request, 'author/author.html')
    else:
        return render(request, 'author/author.html')
