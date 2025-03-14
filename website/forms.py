from django.forms import ModelForm, Select, TextInput, EmailInput, Textarea, NumberInput, DateInput
from . import models 

class CreateClientForm(ModelForm):
    class Meta: 
        model = models.Clientes 
        fields = "__all__"
        widgets = {
            "nome": TextInput(attrs={"placeholder": "Nome do cliente", "class": "form-control w-25"  }),
            "email": EmailInput(attrs={"placeholder": "Email do cliente", "class": "form-control w-25"}),
            "telefone": TextInput(attrs={"placeholder": "Telefone do cliente", "class": "form-control w-25" }),
        }


class CreateProductForm(ModelForm):
    class Meta:
        model = models.Produtos 
        fields = "__all__"
        widgets = {
            "nome": TextInput(attrs={"placeholder": "Nome do produto", "class": "form-control w-25"  }),
            "descricao": Textarea(attrs={"placeholder": "Descrição do produto", "class": "form-control w-25"}),
            "preco": NumberInput(attrs={"placeholder": "Preço do produto", "class": "form-control w-25", "id": "price-input" }),
        }




class CreateOrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Define valores iniciais para os campos
        self.fields['clientes'].initial = models.Pedidos.objects.first()
        self.fields['produtos'].initial = models.Pedidos.objects.first()
    
    class Meta:
        model = models.Pedidos
        fields = "__all__"
        widgets = {
            "clientes": Select(attrs={"class": "form-control w-25", "id": "client-select"}),
            "produtos": Select(attrs={"class": "form-control w-25", "id": "product-select"}),
            "data_pedido": DateInput(attrs={"class": "form-control w-25", "type": "date"}),
        }



class UpdateClientForm(ModelForm):
    class Meta: 
        model = models.Clientes 
        fields = "__all__" 
        widgets = {
            "id": Select(attrs={"autofocus": "autofocus", "disabled": "disabled"})
        }

        
class UpdateProductForm(ModelForm):
    class Meta: 
        model = models.Produtos 
        fields = "__all__" 
        widgets = {
            "id": Select(attrs={"autofocus": "autofocus", "disabled": "disabled"})
        }


class UpdateOrderForm(ModelForm):
    class Meta: 
        model = models.Pedidos 
        fields = "__all__" 
        widgets = {
            "id": Select(attrs={"autofocus": "autofocus", "disabled": "disabled"})
        }


class DeleteClientForm(ModelForm):
    class Meta: 
        model = models.Clientes 
        fields = "__all__"
        widgets = {
            "id": Select(attrs={"autofocus": "autofocus", "disabled": "disabled"})
        }


class DeleteProductForm(ModelForm): 
    class Meta: 
        model = models.Produtos 
        fields = "__all__" 
        widgets = {
            "id": Select(attrs={"autofocus": "autofocus", "disabled": "disabled"})
        }


class DeleteOrderForm(ModelForm):
    class Meta: 
        model = models.Pedidos 
        fields = "__all__"
        widgets = {
            "id": Select(attrs={"autofocus": "autofocus", "disabled": "disabled"})
        }