from django.urls import path
from .views import ClienteView, CreateClienteView


urlpatterns = [
   path('clientes/', ClienteView.as_view(), name='clientes'),
   path('add/', CreateClienteView.as_view(), name='add_cliente'),
]