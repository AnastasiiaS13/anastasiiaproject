from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from .models import Product, Cart, CartItem, Client
from django.contrib.auth.decorators import login_required


def get_cart(request):
    if request.user.is_authenticated:
        try:
            client = Client.objects.get(id=request.user.id)
            cart, created = Cart.objects.get_or_create(client=client)
        except Client.DoesNotExist:
            raise Http404("Client not found.")
    else:
        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)

    return cart


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = get_cart(request)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('view_cart')


def view_cart(request):
    cart = get_cart(request)
    cart_items = cart.items.all()

    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total_price': total_price})


def order_success(request):
    Cart.objects.all().delete()
    messages.success(request, "Your order has been successfully placed.")
    return render(request, 'order_success.html')

@login_required
def remove_from_cart(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id)
    except CartItem.DoesNotExist:
        raise Http404("Product not found")

    cart_item.delete()
    return redirect('view_cart')
