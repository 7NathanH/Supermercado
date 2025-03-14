from django.shortcuts import render
from django.views.generic import TemplateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from . import forms, models 


class IndexView(TemplateView):
    template_name = "index.html"


# creating
class CreatePageView(TemplateView): 
    template_name = "create.html"


class CreateClientView(CreateView):
    template_name = "create_clientes.html"
    model = models.Clientes 
    form_class = forms.CreateClientForm
    success_url = "#"


class CreateProductView(CreateView):
    template_name = "create_produtos.html"
    model = models.Produtos 
    form_class = forms.CreateProductForm
    success_url = "#"


class CreateOrderView(CreateView):
    template_name = "create_pedidos.html"
    model = models.Pedidos 
    form_class = forms.CreateOrderForm
    success_url = "#"


# reading 
class ReadPageView(TemplateView):
    template_name = "read.html"


class ReadClientView(ListView):
    template_name = "read_clientes.html"
    model = models.Clientes 
    context_object_name = "clients"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        
        return context;


class ReadProductView(ListView):
    template_name = "read_produtos.html"
    model = models.Produtos 
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 

        return context;


class ReadOrderView(ListView):
    template_name = "read_pedidos.html"
    model = models.Pedidos 
    context_object_name = "orders"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 

        return context;


# update
class UpdatePageView(TemplateView):
    template_name = "update.html"


class UpdateClientView(UpdateView):
    template_name = "update_clientes.html"
    model = models.Clientes
    form_class = forms.UpdateClientForm 
    success_url = "#"


class UpdateProductView(UpdateView):
    template_name = "update_produtos.html"
    model = models.Produtos
    form_class = forms.UpdateProductForm 
    success_url = "#"


class UpdateOrderView(UpdateView):
    template_name = "update_pedidos.html"
    model = models.Pedidos 
    form_class = forms.UpdateOrderForm 
    success_url = "#"


# delete
class DeleteClientView(DeleteView):
    template_name = "delete_clientes.html"
    model = models.Clientes 
    success_url = "#" 


class DeleteProductView(DeleteView):
    template_name = "delete_produtos.html"
    model = models.Produtos 
    success_url = "#"


class DeleteOrderView(DeleteView):
    template_name = "delete_pedidos.html"
    model = models.Pedidos 
    success_url = "#"