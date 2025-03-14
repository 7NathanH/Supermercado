from django.urls import path
from website import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="indexpage"),

    path("criar/", views.CreatePageView.as_view(), name="createpage"),
    path("criar/cliente/", views.CreateClientView.as_view(), name="createclientpage"),
    path("criar/produto/", views.CreateProductView.as_view(), name="createproductpage"),
    path("criar/pedido/", views.CreateOrderView.as_view(), name="createorderpage"),

    path("listar/", views.ReadPageView.as_view(), name="readpage"),
    path("listar/cliente/", views.ReadClientView.as_view(), name="readclientpage"),
    path("listar/produto/",views.ReadProductView.as_view(), name="readproductpage"),
    path("listar/pedido/", views.ReadOrderView.as_view(), name="readorderpage"),

    path("listar/cliente/atualizar/<int:pk>/", views.UpdateClientView.as_view(), name="updateclientpage"),
    path("listar/produto/atualizar/<int:pk>/", views.UpdateProductView.as_view(), name="updateproductpage"),
    path("listar/pedido/atualizar/<int:pk>/", views.UpdateOrderView.as_view(), name="updateorderpage"),
    
    path("listar/cliente/excluir/<int:pk>/", views.DeleteClientView.as_view(), name="deleteclientpage"),
    path("listar/produto/excluir/<int:pk>/", views.DeleteProductView.as_view(), name="deleteproductpage"),
    path("listar/pedido/excluir/<int:pk>/", views.DeleteOrderView.as_view(), name="deleteorderpage"),
    




]