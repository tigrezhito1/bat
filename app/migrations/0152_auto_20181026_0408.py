# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-26 09:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0151_auto_20181026_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 26, 4, 8, 10, 13212), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
    ]
