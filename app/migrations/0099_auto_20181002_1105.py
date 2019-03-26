# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-02 16:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0098_auto_20180928_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='anios',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 2, 11, 5, 8, 695689), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='hora_instalacion',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 10, 2, 11, 5, 8, 697730), editable=False, max_length=1000, null=True),
        ),
    ]
