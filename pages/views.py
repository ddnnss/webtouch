from django.shortcuts import render
from .models import *

def index(request):
    portfolioItems = PortfolioItem.objects.filter(is_active=True)
    return render(request, 'pages/index.html', locals())

def portfolio(request):
    portfolioItems = PortfolioItem.objects.all()
    filters = Filter.objects.all()
    return render(request, 'pages/portfolio.html', locals())

def portfolio_item(request,nameSlug):
    portfolioItem = PortfolioItem.objects.get(name_slug=nameSlug)
    images = portfolioItem.porfolioItemImages.all()
    return render(request, 'pages/portfolio_item.html', locals())

def prices(request):
    return render(request, 'pages/price.html', locals())

def contacts(request):
    return render(request, 'pages/contacts.html', locals())

def about(request):
    return render(request, 'pages/about.html', locals())