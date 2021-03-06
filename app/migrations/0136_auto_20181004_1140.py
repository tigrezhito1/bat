# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-04 16:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0135_auto_20181004_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 4, 11, 40, 11, 960825), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='hora_instalacion',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 10, 4, 11, 40, 11, 961676), editable=False, max_length=1000, null=True),
        ),
    ]
