# Generated by Django 5.2.2 on 2025-06-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_rename_deposito_movimentacao_id_deposito_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='id_deposito_padrao',
            new_name='deposito_padrao',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='id_fornecedor',
            new_name='fornecedor',
        ),
        migrations.AlterField(
            model_name='produto',
            name='unidade',
            field=models.CharField(choices=[('ml', 'Mililitro'), ('lt', 'Litro'), ('g', 'Grama'), ('kg', 'Quilo'), ('m³', 'Metro cúbico')], max_length=5),
        ),
    ]
