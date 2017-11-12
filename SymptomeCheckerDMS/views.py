from django.shortcuts import render,HttpResponse


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


def welcome(request):
    return HttpResponse('Welcome bitches!')

def fuckyou(request):
    return HttpResponse('Fuck you!')

def test(request):

    return render(
        request,
        'test.html',
        context={},
    )