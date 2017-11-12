from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.views.generic import ListView
from.models import DMSProcedure

# Create your views here.
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # # Генерация "количеств" некоторых главных объектов
    # num_books=Book.objects.all().count()
    # num_instances=BookInstance.objects.all().count()
    # # Доступные книги (статус = 'a')
    # num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    # num_authors=Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={},
    )
def symptom(request):

    return render(
        request,
        'symptom.html',
        context={},
    )
def about(request):

    return render(
        request,
        'about.html',
        context={},
    )
def register(request):

    return render(
        request,
        'register.html',
        context={},
    )
def testbootstrap(request):

    return render(
        request,
        'twbs-bootstrap-2c2ac33\src\pages\index.html',
        context={},
    )


def compute(request):

    return render(request,'register.html')