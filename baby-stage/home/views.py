from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    coisa = "Qualquer coisa"
    context = {
        'coisa': coisa,
    }
    return render(request, 'index.html', context)