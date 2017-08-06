# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id_Comentario', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id_Contacto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=90)),
                ('apellidoP', models.CharField(max_length=45)),
                ('apellidoM', models.CharField(max_length=45)),
                ('cargo', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('comentarios', models.ManyToManyField(blank=True, to='aplicacionobmex.Comentario')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_Curso', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('hora', models.TimeField()),
                ('costo', models.FloatField()),
                ('instructor', models.CharField(max_length=130)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_Direccion', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(blank=True, max_length=50)),
                ('numero', models.CharField(blank=True, max_length=10)),
                ('entidad', models.CharField(blank=True, max_length=30)),
                ('colonia', models.CharField(blank=True, max_length=25)),
                ('delegacion', models.CharField(blank=True, max_length=30)),
                ('pais', models.CharField(blank=True, max_length=30)),
                ('numero_2', models.CharField(blank=True, max_length=30)),
                ('entreCalle_1', models.CharField(blank=True, max_length=30)),
                ('entreCalle_2', models.CharField(blank=True, max_length=30)),
                ('estado', models.CharField(choices=[('AS', 'Aguascalientes'), ('BC', 'Baja California'), ('BS', 'Baja California Sur'), ('CC', 'Campeche'), ('CS', 'Chiapas'), ('CH', 'Chihuahua'), ('CX', 'Ciudad de Mexico'), ('CL', 'Coahuila'), ('CM', 'Colima'), ('DG', 'Durango'), ('EM', 'Estado de Mexico'), ('GT', 'Guanajuato'), ('GR', 'Guerrero'), ('HG', 'Hidalgo'), ('JC', 'Jalisco'), ('MN', 'Michoacan'), ('MS', 'Morelos'), ('NT', 'Nayarit'), ('NL', 'Nuevo Leon'), ('OC', 'Oaxaca'), ('PL', 'Puebla'), ('QT', 'Queretaro'), ('QR', 'Quintana Roo'), ('SP', 'San Luis Potosi'), ('SL', 'Sinaloa'), ('SR', 'Sonora'), ('TC', 'Tabasco'), ('TS', 'Tamaulipas'), ('TL', 'Tlaxcala'), ('VZ', 'Veracruz'), ('YN', 'Yucatan'), ('ZS', 'Zacatecas')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id_Institucion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('rfc', models.CharField(blank=True, max_length=16, null=True)),
                ('direccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_Producto', models.AutoField(primary_key=True, serialize=False)),
                ('generacion', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], unique=True)),
                ('existencias', models.IntegerField(blank=True)),
                ('maxStock', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_Pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('hora', models.TimeField(auto_now=True)),
                ('cantidad', models.IntegerField(default=0)),
                ('monto', models.FloatField()),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Contacto')),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Institucion')),
                ('tipoSilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Inventario')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id_Telefono', models.AutoField(primary_key=True, serialize=False)),
                ('lada', models.IntegerField(blank=True, null=True)),
                ('tipo', models.CharField(max_length=7)),
                ('numero', models.CharField(max_length=13)),
                ('extencion', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='institucion',
            name='telefono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Telefono'),
        ),
        migrations.AddField(
            model_name='curso',
            name='direccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Direccion'),
        ),
        migrations.AddField(
            model_name='curso',
            name='participantes',
            field=models.ManyToManyField(blank=True, to='aplicacionobmex.Contacto'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='cursos',
            field=models.ManyToManyField(blank=True, to='aplicacionobmex.Curso'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='institucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Institucion'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='telefono',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Telefono'),
        ),
    ]
