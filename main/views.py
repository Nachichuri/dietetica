from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomeInfo, ContactInfo, MainCategory, Product

def home(request):

    context = {
        'info': HomeInfo.objects.first(),
        'contact': ContactInfo.objects.first(),
        'categories': MainCategory.objects.all()
    }

    return render(request, 'main/home/index.html', context)

class CategoriesListView(ListView):
    model = MainCategory

class ProductsListView(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product
    category = Product.category