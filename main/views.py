from django.shortcuts import render, redirect

from .forms import ReservationForm
from .models import Category, Product, Slider, About, Offer, Client

def reservation_success(request):
    return render(request, 'reservation_success.html')
# Create your views here.
def home(request):
    form = ReservationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('reservation_success')

    categories = Category.objects.filter(is_visible=True)
    products = Product.objects.filter(is_visible=True)
    slides = Slider.objects.filter(is_visible=True)
    abouts = About.objects.filter(is_visible=True)
    offers = Offer.objects.filter(is_visible=True)
    clients = Client.objects.filter(is_visible=True)

    context = {
        'categories': categories,
        'products': products,
        'slides': slides,
        'abouts': abouts,
        'offers': offers,
        'clients': clients,
        'reservation_form': form,
    }
    return render(request, 'main.html', context=context)
