# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-09 16:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0135_auto_20181004_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='apellido_p',
            field=models.CharField(blank=True, default=1, max_length=1000, verbose_name='Apellido Paterno'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produccion',
            name='cliente',
            field=models.CharField(blank=True, default=1, help_text='Nombre del Cliente', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 11, 4, 0, 477784), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='hora_instalacion',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 10, 9, 11, 4, 0, 480134), editable=False, max_length=1000, null=True),
        ),
    ]
