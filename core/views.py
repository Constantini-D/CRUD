from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto, Usuario
from .forms import ProdutoModelForm, UsuarioModelForm


class IndexView(ListView):
    models = Usuario
    template_name = 'index.html'
    paginate_by = 5
    queryset = Usuario.objects.all()
    ordering = 'id'
    context_object_name = 'usuarios'


class CreateUsuarioView(CreateView):
    model = Usuario
    template_name = 'usuario_form.html'
    fields = ['nome', 'email', 'aniversario']
    success_url = reverse_lazy('index')


class UpdateUsuarioView(UpdateView):
    model = Usuario
    template_name = 'usuario_form.html'
    fields = ['nome', 'email', 'aniversario']
    success_url = reverse_lazy('index')


class DeleteUsuarioView(DeleteView):
    model = Usuario
    template_name = 'usuario_del.html'
    fields = ['nome', 'email', 'aniversario']
    success_url = reverse_lazy('index')


class ProdutoView(ListView):
    models = Produto
    template_name = 'produto.html'
    paginate_by = 5
    ordering = 'id'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('produtos')


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('produtos')


class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('produtos')