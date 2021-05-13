from django.urls import path
from .views import IndexView,CreateUsuarioView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastrar/', CreateUsuarioView.as_view(), name='cadastrar_usuario'),
    path('<int:pk>/update/', UpdateUsuarioView.as_view(), name='upd_usuario'),
    path('<int:pk>/delete/', DeleteUsuarioView.as_view(), name='del_usuario'),

    path('produto/', ProdutoView.as_view(), name='produtos'),
    path('produto_cadastrar/', CreateProdutoView.as_view(), name='cadastrar_produto'),
    path('<int:pk>/produto_delete/', DeleteProdutoView.as_view(), name='del_produto'),
    path('<int:pk>/produto_update/', UpdateProdutoView.as_view(), name='upd_produto'),

]