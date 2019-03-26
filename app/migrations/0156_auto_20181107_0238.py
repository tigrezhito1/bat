# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-07 07:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0155_merge_20181107_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bateria',
            name='cant_bat_usadas',
        ),
        migrations.AddField(
            model_name='atiende',
            name='celular',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='produccion',
            name='motorisado',
            field=models.ForeignKey(blank=True, max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_motorisado', to='app.Atiende'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='almacen',
            field=models.ForeignKey(blank=True, max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_almacen', to='app.Almacen'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='atiende',
            field=models.ForeignKey(blank=True, max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_atiende', to='app.Atiende'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 2, 38, 14, 417661), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='status',
            field=models.ForeignKey(blank=True, max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_status', to='app.Status'),
        ),
    ]
