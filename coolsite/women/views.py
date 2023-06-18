from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']
# Create your views here.
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Главная страница', 'posts': posts})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(request, catid):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=False)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Не нашел</h1>')
