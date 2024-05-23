from django.shortcuts import get_object_or_404, render

from .models import Product

# Create your views here.

def indexx(request):
    products = Product.objects.all() 
    return render(request, 'index.html', {'products': products})

def detailss(request, id):
    product = get_object_or_404(Product, id=id)  
    return render(request, 'details.html', {'product': product})

def index(request):
    return render(request, 'index.html')

def details(request ):
    return render(request, 'details.html')
