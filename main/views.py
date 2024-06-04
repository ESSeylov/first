from django.http import HttpResponse

# Create your views here.
items = [
   {"id": 1, "name": "Кроссовки abibas"},
#    {"id": 2, "name": "Куртка кожаная"},
   {"id": 3, "name": "Coca-cola 1 литр"},
#    {"id": 4, "name": "Картофель фри"},
   {"id": 5, "name": "Кепка"},
]


def home(request):
    text = '''<h1>"Изучаем django"</h1>
            <strong>Автор</strong>: <i>Сейлов Е.С.</i>'''
    return HttpResponse(text)


def about(request):
    text = '''Имя: <strong>Иван</strong>
            <br>Отчество: <strong>Петрович</strong>
            <br>Фамилия: <strong>Иванов</strong>
            <br>телефон: <strong>8-923-600-01-02</strong>
            <br>email: <strong>vasya@mail.ru</strong>'''
    return HttpResponse(text)


def get_item(request, item_id):
    for i in items:
        if int(i['id']) == int(item_id):
            item = str(i['name']) + '<br>'
            item += '''<br><a href="/items">Назад к списку товаров</a>'''
            return HttpResponse(item)
    else:
        item = (f'''Товар с id={item_id} не найден<br>
                <br><a href="/items">Назад к списку товаров</a>''')
    return HttpResponse(item)


def get_items(request):
    i = ([f"""<a href="{item['id']}">{item['id']}. {item['name']}</a>"""+'<br>'
          for item in items])
    return HttpResponse(i)
