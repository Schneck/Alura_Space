from django.shortcuts import render, redirect
from apps.usuario.forms import LoginForms, CadastroForms, LogoutForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logou com sucesso!')
            return redirect ('index')
        else:
            messages.error(request, f'Usuario {nome}, não cadastrado. Tente novamente!')
            return redirect ('login')
        
    return render(request, 'usuario/login.html', {'form':form})

def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome=form['nome_cadastro'].value()
            email=form['email1'].value()
            senha=form['senha1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, f'Usuario {nome} já existe, insira um nome diferente!')
                return redirect ('cadastro')
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, f'Usuario {nome}, cadastrado com sucesso!')
            return redirect ('login')

            

    return render(request, 'apps/usuario/cadastro.html', {'form':form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Usuario deslogado com Sucesso!')
    return redirect('login')