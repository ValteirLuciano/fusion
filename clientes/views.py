from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteModelForm


# Create your views here.
class ClienteView(ListView):
    model = Cliente
    template_name = 'testimunha_clientes.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'


class CreateClienteView(CreateView):
    model = Cliente
    template_name = 'cliente_form.html'
    form_class = ClienteModelForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        obj = form.save(commit=False)
        return super(CreateClienteView, self).form_valid(form)
