from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Produto, Usuario
from .forms import ProdutoModelForm, UsuarioModelForm


class IndexView(ListView):
    models = Usuario
    template_name = 'index.html'
    queryset = Usuario.objects.all()
    context_object_name = 'usuarios'