from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer


class ProductoListView(ListAPIView):
    queryset = Producto.objects.order_by('nombre')
    serializer_class = ProductoSerializer

class ProductoCreateView(CreateAPIView):
    serializer_class = ProductoSerializer

class CategoriaListView(ListAPIView):
    queryset = Categoria.objects.order_by('nombre')
    serializer_class = CategoriaSerializer

class CategoriaCreateView(CreateAPIView):
    serializer_class = CategoriaSerializer

"""

def index(request):
    product_list = Producto.objects.order_by('nombre')
    curso_list = Curso.objects.order_by('nombre')
    categorias = Categoria.objects.order_by('nombre')
    context = {'product_list': product_list, 'curso_list': curso_list, 'categoria_list': categorias}
    return render(request, 'index.html', context)
"""
"""
def producto(request):
    return render(request, 'producto.html')
"""