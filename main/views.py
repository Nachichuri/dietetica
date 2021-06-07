from django.shortcuts import render
from .models import HomeInfo

def home(request):

    context = {
        'info': HomeInfo.objects.first(),
    }

    return render(request, 'main/home/index.html', context)