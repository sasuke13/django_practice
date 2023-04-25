from django.urls import path
from .views import main_page, get_all_users, get_certain_user

urlpatterns = [
    path("", main_page, name="users"),
    path("all_users/", get_all_users, name="all_users"),
    path("certain_user/", get_certain_user, name="certain_user"),
]