from django.shortcuts import render
from store.models import Item
# Create your views here.

# items = [
#     {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
#     {"id": 2, "name": "Куртка кожаная", "quantity": 2},
#     {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
#     {"id": 4, "name": "Картофель фри", "quantity": 0},
#     {"id": 5, "name": "Кепка", "quantity": 124},
# ]


def get_item(request, item_id):
    query_items = Item.objects.all()
    for i in query_items:
        if int(i.id) == int(item_id):
            if i.quantity > 0:
                # item = (f'''{i["name"]}<br></br>
                #         Количество: {i["quantity"]}<br>''')
                context = {"item": i}
            else:
                # item = f'''{i["name"]}<br></br>Только по предзаказу<br>'''
                context = {"item": i}
            return render(request, "item_detail_page.html", context)
    else:
        # item = f"""Товар с id={item_id} не найден<br>"""
        i = {"id": item_id, "name": f"""Товар с id={item_id} не найден"""}
        context = {"item": i}
    return render(request, "item_detail_page.html", context)


def get_items(request):
    query_items = Item.objects.all()
    # list_items = "".join(
    #     [
    #         f"""<a href="{item['id']}">{item['id']}.
    #                        {item['name']}</a><br>"""
    #         for item in items
    #     ]
    # )
    context = {
        "list_items": query_items,
    }
    return render(request, "items_list_page.html", context)
