from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart, order_success

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('order_success/', order_success, name='order_success'),
]
