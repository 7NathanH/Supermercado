
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('descricao', models.CharField(max_length=45)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'produtos',
            },
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateField()),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.clientes')),
                ('produtos', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.produtos')),
            ],
            options={
                'db_table': 'pedidos',
            },
        ),
    ]