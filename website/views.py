from django.shortcuts import render, redirect
from website.models import Pessoa, Ideia

# Create your views here.

def index(request):
    contexto = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        contexto = {'msg': 'Parabéns :)'}
        return render(request, 'login.html', contexto)

    return render(request, 'index.html', contexto)

def cadastro_existente(request):   
    contexto = {} 
    return render(request, 'login.html', contexto)


def sobre(request):
    ideias = Ideia.objects.filter(ativo = True).all()
    contexto = {
        'ideias': ideias
    }
    return render(request, 'sobre.html', contexto)

def remover_ideia(request, id):
    ideia = Ideia.objects.filter(id=id).first()
    if ideia is not None:
        ideia.ativo = False
        ideia.save()
        return redirect('/sobre')
    return render(request, 'sobre.html', {'msg': 'Ops , não foi dessa vez'})

def login(request):
    if request.method == 'POST':
        email_form = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_form).first()

        print('Iae meu bom amigo ', pessoa)

        if pessoa is None:
            contexto = {'msg': 'Cadastre-se para criar uma ideia'}
            return render(request, 'index.html', contexto)
        else:
            contexto = {'pessoa': pessoa}
            return render(request, 'ideias.html', contexto)

    return render(request, 'login.html', {})

def cadastrar_ideia(request):
    if request.method == 'POST':
        email_pessoa = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_pessoa).first()
        if pessoa is not None:
            ideia = Ideia()
            ideia.pessoa = pessoa
            ideia.titulo = request.POST.get('titulo')
            ideia.descricao = request.POST.get('descricao')
            ideia.categorias = request.POST.get('categorias')
            ideia.categoria_outros = request.POST.get('categoria_outros')
            ideia.save()
            print('uhuuu')
            return redirect('/sobre') 

    return render(request, 'ideias.html', {})

