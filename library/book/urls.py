from django.urls import path
from .views import book_index, get_book_list, create_book, get_book_info, book_update, delete_book, \
    get_certain_user_order, get_id

urlpatterns = [
    path('', book_index, name='book'),
    path('book_list/', get_book_list, name='book'),
    path('create_book/', create_book, name='create_book'),
    path('book_info/<int:id>/', get_book_info, name='get_book_info'),
    path('book_info/<int:id>/book_update', book_update, name='book_update'),
    path('book_info/<int:id>/delete', delete_book, name='delete_book'),
    path('book_list/certain_user', get_id, name='get_id'),
    path('book_list/<int:id>/certain_user', get_certain_user_order, name='get_certain_user_order'),


]
