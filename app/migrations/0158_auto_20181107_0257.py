# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-07 07:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0157_auto_20181107_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='motorisado',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 2, 57, 23, 461912), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
    ]
