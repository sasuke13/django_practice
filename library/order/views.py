from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views import generic

import datetime

from .models import Book, Order, CustomUser
from authentication.models import  CustomUser
from book.models import Book


def get_all_orders(request):
    usr = request.user
    if usr.is_superuser:
        return render(request, "order.html", {"text": Order.get_all()})
    else:
        orders = []
        for order in Order.get_all():
            if order.user == request.user:
                orders.append(order)
        return render(request, "order.html", {"text": orders})


def create_order(request):
    if request.method == "GET":
        return render(request, 'order.html')
    if request.method == "POST":
        order = Order()
        usr = CustomUser()
        book = Book()
        user_id = request.user
        book_id = int(request.POST['book_id'])
        plated_end_at = request.POST['plated_end_at']
        usr = usr.get_by_id(user_id.id)
        book = book.get_by_id(book_id)

        order.create(user=usr, book=book, plated_end_at=plated_end_at)

        return redirect('order')


def delete_order(request, id):
    order = Order()
    if request.method == "POST":
        order = order.get_by_id(id)
        if order.end_at == None:
            order.end_at = datetime.datetime.now()
            order.save()
            return redirect('order')
    else:
        return render(request, "order.html")


def update_order(request, id):
    order = Order.get_by_id(id)

    if request.method == "GET":
        return render(request, 'order.html', {'text': order})
    if request.method == "POST":
        plated_end_at = request.POST.get('plated_end_at')
        end_at = request.POST('end_at')
        order.update(end_at=end_at, plated_end_at=plated_end_at)
        return redirect('order', id=order.id)


def get_user_orders(request):
    search_term = request.GET.get('searchTerm', '')
    orders = Order.objects.all()

    if search_term:
        orders = orders.filter(Q(name__icontains=search_term) |
                             Q(description__icontains=search_term) |
                             Q(authors__name__icontains=search_term))

    context = {
        'orders': orders
    }

    return render(request, 'order.html', context)


def get_order_info(request, id):
    if request.method == 'GET':
        order = Order.get_by_id(id)
        return render(request, 'order_info.html', {'order': order})
    else:
        return render(request, 'order.html')
