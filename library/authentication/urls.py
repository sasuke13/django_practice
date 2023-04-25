from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('registration/', views.auth_register_user, name='register'),
    path('logout/', views.logout_user, name='logout')
]