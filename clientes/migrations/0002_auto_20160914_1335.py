# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='calle',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='numero_exterior',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='numero_interior',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]