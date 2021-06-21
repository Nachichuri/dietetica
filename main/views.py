from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import HomeInfo, ContactInfo, MainCategory, Product

# Home view

def home(request):

    context = {
        'info': HomeInfo.objects.first(),
        'contact': ContactInfo.objects.first(),
        'categories': MainCategory.objects.all()
    }

    return render(request, 'main/home/index.html', context)


# Class based views for products indexing

class CategoriesListView(ListView):
    model = MainCategory

class ProductsListView(ListView):

    def get_queryset(self):
        if self.kwargs['pk'] in [category.slug for category in MainCategory.objects.all()]:
            return Product.objects.filter(category=self.kwargs['pk'])
        else:
            raise Http404


class ProductDetail(DetailView):
    
    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs['pk'])