# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionobmex', '0008_auto_20170721_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='id_Comentario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='id_Contacto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id_Curso',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='id_Direccion',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='id_Institucion',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='id_Producto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='id_Pedido',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='id_Telefono',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]