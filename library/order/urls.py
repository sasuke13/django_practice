from django.urls import path
from .views import create_order, update_order, delete_order,get_all_orders, get_order_info
urlpatterns = [
    path('', get_all_orders, name='order'),
    path('create_order/', create_order, name='create_order'),
    path('order_info/<int:id>/', get_order_info, name='get_order_info'),
    path('order_info/<int:id>/delete_order/', delete_order, name='delete_order'),
    path('order_info/<int:id>/update_order/', update_order, name='update_order'),
]