# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 02:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionobmex', '0002_auto_20170709_2105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='tipo',
            new_name='generacion',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='enstock',
        ),
    ]
