from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Livro

def index(request):
    livros = Livro.objects.all()
    contexto ={
        'livros': livros
    }
    return render(request, 'index.html', contexto)

def home(request):
    return render(request, 'home.html')

def estoque(request):
    livros = Livro.objects.all()
    contexto = {
        'livros': livros
    }
    return render(request, 'estoque.html', contexto)

def contato(request):
    return render(request, 'contato.html')

def equipe(request):
    return render(request, 'equipe.html')

def create(request):
    if request.method == 'POST':
        livro = Livro()
        livro.titulo = request.POST.get('titulo')
        livro.autor = request.POST.get('autor')
        livro.editora = request.POST.get('editora')
        livro.genero = request.POST.get('genero')
        livro.preco = request.POST.get('preco')
        livro.tipo = request.POST.get('tipo')
        livro.save()
    return HttpResponseRedirect('/crudapp/index')

def create_template(request):
    return render(request,'create.html')

def read(request, livro_id):
    if request.method == 'GET':
        livros = Livro.objects.filter(id=livro_id)
        contexto = {
            'livros': livros
        }
        return render(request, 'read.html', contexto)

def update_template(request, livro_id):
    if request.method == 'GET':
        livros = Livro.objects.filter(id=livro_id)
        contexto = {
            'livros': livros
        }
        return render(request, 'update.html', contexto)

def update(request):
    if request.method == 'POST':
        livro_id = request.POST.get('livro_id')
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        editora = request.POST.get('editora')
        genero = request.POST.get('genero')
        preco = request.POST.get('preco')
        tipo = request.POST.get('tipo')
        livro = Livro.objects.filter(id=livro_id)
        livro.update(titulo=titulo, autor=autor, editora=editora, genero=genero, preco=preco, tipo=tipo)
        return HttpResponseRedirect('/crudapp/index')

def delete(request, livro_id):
    if request.method == 'GET':
        livro = Livro.objects.filter(id=livro_id)
        livro.delete()

        return HttpResponseRedirect('/crudapp/index')