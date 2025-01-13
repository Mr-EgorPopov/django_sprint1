from django.shortcuts import render
from django.http import HttpResponse


def about(request) -> HttpResponse:
    """Отрисовка страницы 'О проекте'"""
    template = 'pages/about.html'
    context = {'active_page': 'about'}
    return render(request, template, context)


def rules(request) -> HttpResponse:
    """Отрисовка страницы 'Наши Правила'"""
    template = 'pages/rules.html'
    context = {'active_page': 'rules'}
    return render(request, template, context)
