from django.urls import path, include
from .views import main_form, get_all, create_author, delete_author

urlpatterns = [
    path('', main_form, name='author'),
    path('get_all/', get_all, name='get_all_authors'),
    path('create/', create_author, name='create_an_author'),
    path('delete/', delete_author, name='delete_an_author')
]