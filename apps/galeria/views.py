from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from apps.galeria.models import Fotografia
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Sem permissão para navegar, você deve estar logado!')
        return redirect ('login')
    fotografias = Fotografia.objects.order_by('-data_publicacao').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Sem permissão para navegar, você deve estar logado!')
        return redirect ('login')
    fotografias = Fotografia.objects.order_by('-data_publicacao').filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})

def super_nova(request):
    
    
    return render(request, 'galeria/super_nova.html')