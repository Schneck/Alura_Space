from django.urls import path
from apps.galeria.views import index, imagem, buscar, super_nova

urlpatterns = [
    path('', index, name= 'index'),
    path('imagem/<int:foto_id>', imagem, name= 'imagem'),
    path('buscar', buscar, name='buscar'),
    path('super_nova/', super_nova, name='super_nova'),
]