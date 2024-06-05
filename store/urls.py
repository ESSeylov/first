from django.urls import path
from store import views

urlpatterns = [
    path('', views.get_items, name='items'),
    path('<int:item_id>', views.get_item, name='item'),
]
