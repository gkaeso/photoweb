from django.shortcuts import render

from .resources import KEYS


def index(request):
    return render(request, 'website/index.html', { "keys" : KEYS })

def portfolio(request):
    return render(request, 'website/portfolio.html', { "keys" : KEYS })