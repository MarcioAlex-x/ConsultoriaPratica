from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('download/consultoria/<int:id>/', views.download_revista_consultoria, name='download_revista_consultoria'),
    path('download/espaco/<int:id>/', views.download_revista_espaco, name='download_revista_espaco'),
    path('download/avon/<int:id>/', views.download_revista_avon, name='download_revista_avon'),
    path('download/estilo/<int:id>/', views.download_revista_estilo, name='download_revista_estilo'),  
     path('download/imagem-combo/<int:id>/', views.download_imagem_combo, name='download_imagem_combo'),   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)