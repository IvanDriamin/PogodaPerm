from django.shortcuts import render
from . import parser

def index(request):
    return render(request, 'weather/index.html', parser.mas)
