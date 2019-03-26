# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-11 13:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0144_auto_20181010_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 11, 8, 58, 53, 19550), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='hora_instalacion',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 10, 11, 8, 58, 53, 20534), editable=False, max_length=1000, null=True),
        ),
    ]