from django.shortcuts import render
from .models import HomeInfo, ContactInfo, MainCategories

def home(request):

    context = {
        'info': HomeInfo.objects.first(),
        'contact': ContactInfo.objects.first(),
        'categories': MainCategories.objects.all()
    }

    return render(request, 'main/home/index.html', context)