# Generated by Django 5.0.3 on 2024-03-22 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_pedido_pedidos_rename_produto_produtos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produtos', models.JSONField()),
            ],
        ),
    ]
