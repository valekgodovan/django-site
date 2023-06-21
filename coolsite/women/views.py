from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


# Create your views here.
def index(request):
    posts = Women.objects.all()
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse('add page')


def contact(request):
    return HttpResponse('contacts')


def login(request):
    return HttpResponse('login')


def show_post(request, post_id):
    return HttpResponse(f'Статья с id = {post_id}')


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404

    context = {
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'posts': posts,
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Не нашел</h1>')
