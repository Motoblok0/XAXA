from django.shortcuts import render
from django.http import HttpResponse
from .models import advertisement

def index(request):
    advertisements = advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context=context)

def top_sellers(request):
    return render(request, 'top-sellers.html')