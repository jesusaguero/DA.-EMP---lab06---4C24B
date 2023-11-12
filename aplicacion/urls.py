from django.urls import path

from .views import (CategoriaCreateView, CategoriaListView, ProductoCreateView,
                    ProductoListView)

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('productos/create/', ProductoCreateView.as_view(), name='producto-create'),
    path('productos/<int:pk>/', ProductoCreateView.as_view(), name='producto-update'),
    path('productos/<int:pk>/delete/', ProductoCreateView.as_view(), name='producto-delete'),
    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/create/', CategoriaCreateView.as_view(), name='categoria-create'),
    path('categorias/<int:pk>/', CategoriaCreateView.as_view(), name='categoria-update'),
    path('categorias/<int:pk>/delete/', CategoriaCreateView.as_view(), name='categoria-delete'),
    ]
