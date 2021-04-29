from django.shortcuts import render

from .resources import KEYS


def index(request):
    return render(request, 'website/index.html', { "keys" : KEYS })