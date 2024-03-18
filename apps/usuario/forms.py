from typing import Any
from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label = 'Login Name',
        required = True,
        max_length = 70,
        widget = forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: Nickname ou CPF"
            }
        )
    )
    senha = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: Digite sua senha"

            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label = 'Digite Seu Nome Completo',
        required = True,
        max_length = 70,
        widget = forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: Nickname ou CPF"
            }
        )
    )
    email1=forms.EmailField(
        label = 'Qual Email',
        required = True,
        max_length = 70,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: schneck@xpto.com"
            }
        )
    )
    email2=forms.EmailField(
        label = 'Confirme seu Email',
        required = True,
        max_length = 70,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: digite seu email novamente"
            }
        )
    )
    senha1 = forms.CharField(
        label = 'Digite uma Senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: Digite sua senha"

            }
        )
    )
    senha2 = forms.CharField(
        label = 'Confirmar Senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: Digite sua senha outra vez"

            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError('Espaços não são permitidos neste campo!')
            else:
                return nome

    def clean_senha2(self):
        senha1 = self.cleaned_data.get('senha1')
        senha2 = self.cleaned_data.get('senha2')
        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha2
    
    def clean_email2(self):
        email1 = self.cleaned_data.get('email1')
        email2 = self.cleaned_data.get('email2')
        if email1 and email2:
            if email1 != email2:
                raise forms.ValidationError('Emails não são idênticos')
            else:
                return email2

class LogoutForms(forms.Form):
    exit = forms.CharField(
        label = 'Digite sua senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
        )
    )

