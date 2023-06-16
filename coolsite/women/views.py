from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('страница приложения women.')

def categories(request):
    return HttpResponse('<h1>статьи по категориям</h1>')
