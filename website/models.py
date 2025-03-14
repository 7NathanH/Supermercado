from django.db import models


class Clientes(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=45)

    class Meta:
        
        db_table = 'clientes'

    def __str__(self):
        return self.nome


class Pedidos(models.Model):
    clientes = models.ForeignKey('Clientes', models.DO_NOTHING)
    produtos = models.ForeignKey('Produtos', models.DO_NOTHING)
    data_pedido = models.DateField()

    class Meta:
         
        db_table = 'pedidos'

    def __str__(self):
        return self.nome

    


class Produtos(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        
        db_table = 'produtos'

    def __str__(self):
        return self.nome 