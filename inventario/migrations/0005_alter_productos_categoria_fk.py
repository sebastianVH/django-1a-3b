# Generated by Django 4.0.7 on 2023-09-28 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_alter_productos_categoria_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='categoria_fk',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.categorias'),
        ),
    ]
