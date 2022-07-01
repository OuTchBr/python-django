from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produto/cadastro/', views.cadastro, name='cadastro'),
    path('produto/editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('produto/remover/<int:pk>/', views.remover_produto, name='remover_produto'),
    
]