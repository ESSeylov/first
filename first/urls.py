from django.urls import include, path
from main import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('items/', include('store.urls'))
]
