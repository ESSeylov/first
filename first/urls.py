from django.urls import include, path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('items/', include('store.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
