from django import forms

from .models import Produto, Usuario


class UsuarioModelForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'


class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'

