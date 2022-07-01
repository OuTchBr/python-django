from operator import ge
from django.shortcuts import redirect, render
from datetime import datetime
# Create your views here.
from django.http import HttpResponse
from .models import Produto
from .forms import ProdutoForm
from django.shortcuts import render, redirect


def index(request):
    agora = datetime.now()
    context = {
        'agora': agora, 
    }
    return render(request, 'index.html', context)


def lista_produtos(request):
    context = {
        'lista':Produto.objects.all(),
    }
    
    return render(request, 'produto/lista.html', context)

def cadastro(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            f = ProdutoForm(request.POST)
            if f.is_valid():
                produto = f.save(commit=False)
                produto.nome = f.data['nome']
                produto.preco = f.data['preco']
                produto.save()
                return redirect('lista_produtos')
        else:
            f = ProdutoForm()

        agora = datetime.now()
        context = {
            'form':f,
            'agora':agora,
        }
        return render(request, 'produto/cadastro.html', context)
    else:
        return redirect('lista_produtos')

def editar_produto(request, pk):
    if request.user.is_authenticated:    
        produto = Produto.objects.get(pk=pk)
        form = ProdutoForm(instance=produto)

        if request.method == 'POST':
            form = ProdutoForm(request.POST, instance=produto)

            if form.is_valid():
                produto = form.save(commit=False)
                produto.nome = form.data['nome']
                produto.preco = form.data['preco']
                produto.save()
                return redirect('lista_produtos')
        else:
            form = ProdutoForm(instance=produto)

        context = {
            'form':form,
        }
        return render(request, 'produto/cadastro.html', context)
    else:
        return redirect('lista_produtos')
    
def remover_produto(request, pk):
    if request.user.is_authenticated: 
        produto = Produto.objects.get(pk=pk)

        if request.method == 'POST':
            produto.delete()
            return redirect('lista_produtos')

        return render(request,  'produto/remover.html', {'produto':produto})
    else:
        return redirect('lista_produtos')