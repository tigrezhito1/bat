# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-13 14:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0159_auto_20181109_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produccion',
            name='direccion1',
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 13, 9, 29, 40, 572643), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
    ]