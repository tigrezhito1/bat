# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-03 14:26
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'accion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_personal', models.IntegerField(blank=True, null=True)),
                ('meta_requerida', models.IntegerField(blank=True, null=True)),
                ('meta_equipo', models.IntegerField(blank=True, null=True)),
                ('fecha_ingreso', models.DateTimeField(blank=True, null=True)),
                ('correo_capital', models.CharField(blank=True, max_length=1000, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='static')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=1000, null=True)),
                ('dni', models.CharField(blank=True, max_length=1000, null=True)),
                ('direccion', models.CharField(blank=True, max_length=1000, null=True)),
                ('telefono', models.CharField(blank=True, max_length=1000, null=True)),
                ('telefono_1', models.CharField(blank=True, max_length=1000, null=True)),
                ('relacion_contacto', models.CharField(blank=True, max_length=1000, null=True)),
                ('telefono_contacto_emergencia', models.CharField(blank=True, max_length=1000, null=True)),
                ('contacto_emergencia', models.CharField(blank=True, max_length=1000, null=True)),
                ('correo_personal', models.CharField(blank=True, max_length=1000, null=True)),
                ('movil_contacto', models.CharField(blank=True, max_length=1000, null=True)),
                ('version', models.CharField(blank=True, max_length=1000, null=True)),
                ('codigo', models.CharField(blank=True, max_length=1000, null=True)),
                ('tipo_movil', models.CharField(blank=True, max_length=1000, null=True)),
                ('asesor_anterior', models.CharField(blank=True, max_length=1000, null=True)),
                ('modelo', models.CharField(blank=True, max_length=1000, null=True)),
                ('version_movil', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Agente',
                'db_table': 'agente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Agentecliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'agentecliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Agentejerarquia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Agente / Jerarquia',
                'db_table': 'agentejerarquia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruta', models.FileField(max_length=100000, upload_to='static')),
                ('nombre', models.CharField(blank=True, max_length=10000, null=True)),
                ('tipo_archivo', models.CharField(choices=[('Formulario', 'Formulario'), ('Comercial', 'Comercial')], max_length=1000)),
                ('peru', models.BooleanField(default=False)),
                ('ecuador', models.BooleanField(default=False)),
                ('colombia', models.BooleanField(default=False)),
                ('estados_unidos', models.BooleanField(default=False, verbose_name='Estados Unidos')),
                ('bolivia', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Biblioteca',
                'db_table': 'archivos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('nacimiento', models.CharField(blank=True, max_length=1000, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True, verbose_name='Correo personal')),
                ('correo_capital', models.CharField(blank=True, max_length=1000, null=True)),
                ('fecha_ingreso', models.DateTimeField(blank=True, null=True)),
                ('meta_personal', models.IntegerField(blank=True, null=True)),
                ('meta_requerida', models.IntegerField(blank=True, null=True)),
                ('dni', models.CharField(blank=True, max_length=1000, null=True)),
                ('direccion', models.CharField(blank=True, max_length=1000, null=True)),
                ('telefono', models.CharField(blank=True, max_length=1000, null=True)),
                ('contacto', models.CharField(blank=True, max_length=1000, null=True)),
                ('relacion', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Relacion del contacto')),
                ('movil_contacto', models.CharField(blank=True, max_length=1000, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='static')),
            ],
            options={
                'verbose_name': 'Datos de los Usuario',
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cierres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField()),
                ('observacion', models.CharField(blank=True, max_length=10000, null=True)),
                ('fecha_solicitud', models.DateTimeField(blank=True, null=True)),
                ('prima_target', models.CharField(blank=True, max_length=1000, null=True)),
                ('prima_anual', models.CharField(blank=True, max_length=1000, null=True)),
                ('fecha_poliza', models.DateTimeField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField()),
                ('inforce', models.BooleanField()),
                ('agente_equipo', models.IntegerField(blank=True, null=True)),
                ('numero_poliza', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Cierre',
                'db_table': 'citas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateTimeField()),
                ('observacion', models.CharField(blank=True, max_length=10000, null=True)),
                ('fecha_solicitud', models.DateTimeField(blank=True, null=True)),
                ('prima_target', models.CharField(blank=True, max_length=1000, null=True)),
                ('prima_anual', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_poliza', models.DateTimeField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('inforce', models.BooleanField(default=False)),
                ('agente_equipo', models.IntegerField(blank=True, null=True)),
                ('numero_poliza', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Numero Poliza')),
                ('cliente_cita_equipo', models.CharField(blank=True, max_length=1000, null=True)),
                ('propuesta_cita_equipo', models.CharField(blank=True, max_length=1000, null=True)),
                ('cliente_antiguo', models.CharField(blank=True, default='No', max_length=1000, null=True)),
                ('upload_csv', models.BooleanField(default=0)),
                ('asesor_anterior', models.CharField(blank=True, max_length=10000, null=True)),
                ('valida_pos', models.BooleanField(default=0)),
                ('upload_csv_julio_enero_2019', models.BooleanField(default=0)),
                ('upload_ene_jul_2019_ecu', models.BooleanField(default=0)),
            ],
            options={
                'ordering': ('agente',),
                'verbose_name': 'Cita',
                'db_table': 'citas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Cliente')),
                ('apellido', models.CharField(blank=True, max_length=1000, null=True)),
                ('email', models.CharField(blank=True, max_length=1000, null=True)),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=1000, null=True)),
                ('direccion', models.CharField(blank=True, max_length=1000, null=True)),
                ('numero_hijos', models.IntegerField(blank=True, null=True)),
                ('dni', models.CharField(blank=True, max_length=1000, null=True)),
                ('conyuge', models.CharField(blank=True, max_length=1000, null=True)),
                ('edad_conyuge', models.IntegerField(blank=True, null=True)),
                ('fecha_nacimiento_conyuge', models.DateField(blank=True, null=True)),
                ('upload_csv', models.BooleanField(default=0)),
                ('upload_csv_julio_enero_2019', models.BooleanField(default=0)),
                ('upload_ene_jul_2019_ecu', models.BooleanField(default=0)),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Cliente',
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Compania')),
            ],
            options={
                'verbose_name': 'Compania',
                'db_table': 'compania',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Equipo',
                'db_table': 'equipo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'estado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10000)),
            ],
            options={
                'verbose_name': 'Estado Civil',
                'db_table': 'estado_civil',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estructura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Estructura',
                'db_table': 'estructura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'grupo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Iconos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=10000, null=True)),
                ('icono', models.CharField(blank=True, max_length=10000, null=True)),
            ],
            options={
                'verbose_name': 'Icono',
                'db_table': 'iconos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jerarquia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'jerarquia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=1100)),
            ],
            options={
                'db_table': 'log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000, verbose_name='Mes')),
            ],
            options={
                'verbose_name': 'Mes',
                'db_table': 'mes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Forma Pago',
                'db_table': 'modalidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('descripcion', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'nivel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField(blank=True, max_length=10000, null=True)),
            ],
            options={
                'db_table': 'notificacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Paise',
                'db_table': 'pais',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParientesCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Parientes del Cliente',
                'db_table': 'parientes_cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField()),
                ('observacion', models.CharField(blank=True, max_length=10000, null=True)),
                ('fecha_solicitud', models.DateTimeField(blank=True, null=True)),
                ('prima_target', models.IntegerField(blank=True, max_length=1000, null=True)),
                ('prima_anual', models.IntegerField(blank=True, max_length=1000, null=True)),
                ('fecha_poliza', models.DateTimeField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField()),
                ('inforce', models.BooleanField()),
                ('agente_equipo', models.IntegerField(blank=True, null=True)),
                ('numero_poliza', models.CharField(blank=True, max_length=1000, null=True)),
                ('upload_csv', models.BooleanField(default=0)),
                ('asesor_anterior', models.CharField(blank=True, max_length=10000, null=True)),
                ('valida_pos', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': 'POS',
                'db_table': 'citas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Producto',
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PropuestaCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(max_length=10000)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('detalle', models.CharField(max_length=1000)),
                ('inforce', models.BooleanField()),
                ('interes', models.CharField(blank=True, max_length=1000, null=True)),
                ('upload_csv', models.BooleanField(default=0)),
                ('upload_csv_julio_enero_2019', models.BooleanField(default=0)),
                ('upload_ene_jul_2019_ecu', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'propuesta_cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ramo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10000)),
            ],
            options={
                'db_table': 'ramo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RamoCompaniaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antiguo', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'ramo_compania_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'relacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Semanas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=1000)),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True)),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
                ('anio', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Semana',
                'db_table': 'semanas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Statuspoliza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Status Poliza',
                'db_table': 'status_poliza',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subgrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'subgrupo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TelefonoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Telefonos del Usuario',
                'db_table': 'telefono_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoAgente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10000)),
            ],
            options={
                'verbose_name': 'Tipos de Agente',
                'db_table': 'tipo_agente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Tipos de Cita',
                'db_table': 'tipo_cita',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoSeguimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Tipos de Seguimiento',
                'db_table': 'tipo_seguimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Atiende',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bateria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=1000, null=True)),
                ('equivalencia', models.CharField(blank=True, max_length=1000, null=True)),
                ('cantidad', models.CharField(blank=True, max_length=1000, null=True)),
                ('marca', models.CharField(blank=True, max_length=1000, null=True)),
                ('modelo', models.CharField(blank=True, max_length=1000, null=True)),
                ('precio', models.CharField(blank=True, max_length=1000, null=True)),
                ('cant_bat_usadas', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_social', models.CharField(blank=True, max_length=1000, null=True)),
                ('ruc', models.CharField(blank=True, max_length=1000, null=True)),
                ('direc_r_social', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
                ('apellido', models.CharField(blank=True, max_length=300)),
                ('dni', models.CharField(blank=True, max_length=300)),
                ('domicilio', models.CharField(blank=True, max_length=300, null=True)),
                ('telefono', models.CharField(blank=True, max_length=300)),
                ('celular', models.CharField(blank=True, max_length=300)),
                ('email', models.CharField(blank=True, max_length=300, null=True)),
                ('referenciado', models.CharField(blank=True, max_length=300)),
                ('nacimiento', models.DateTimeField(blank=True, null=True)),
                ('fecha_ini', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Ingreso')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime(2018, 9, 3, 14, 26, 20, 161212), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)')),
                ('telefono_1', models.CharField(blank=True, help_text='N\xfamero de tel\xe9fono desde donde llama el cliente', max_length=1000, null=True)),
                ('telefono_2', models.CharField(blank=True, help_text='Otro nmero de tel\xe9fono de contacto', max_length=1000, null=True)),
                ('cliente', models.CharField(blank=True, help_text='Nombre del Cliente', max_length=1000, null=True)),
                ('apellido_m', models.CharField(blank=True, max_length=1000, null=True)),
                ('apellido_p', models.CharField(blank=True, max_length=1000, null=True)),
                ('dni', models.CharField(blank=True, help_text='Otro nmero de dni', max_length=1000, null=True)),
                ('direccion', models.CharField(blank=True, max_length=1000, null=True)),
                ('version', models.CharField(blank=True, max_length=1000, null=True)),
                ('serie', models.CharField(blank=True, max_length=1000, null=True)),
                ('anio', models.CharField(blank=True, max_length=1000, null=True)),
                ('motor', models.CharField(blank=True, max_length=1000, null=True)),
                ('cilindrada', models.CharField(blank=True, max_length=1000, null=True)),
                ('color', models.CharField(blank=True, max_length=1000, null=True)),
                ('kilometraje', models.CharField(blank=True, max_length=1000, null=True)),
                ('placa', models.CharField(blank=True, max_length=1000, null=True)),
                ('cantidad', models.CharField(blank=True, max_length=1000, null=True)),
                ('marca_producto', models.CharField(blank=True, max_length=1000, null=True)),
                ('modelo_bateria', models.CharField(blank=True, max_length=1000, null=True)),
                ('precio', models.CharField(blank=True, max_length=1000, null=True)),
                ('cantidad_bu', models.CharField(blank=True, help_text='Cantidad de baterias usadas', max_length=1000, null=True)),
                ('descuento', models.CharField(blank=True, max_length=1000, null=True)),
                ('precio_total', models.CharField(blank=True, max_length=1000, null=True)),
                ('fecha_atencion', models.DateField(blank=True, max_length=1000, null=True)),
                ('hora_instalacion', models.TimeField(blank=True, max_length=1000, null=True)),
                ('misma_direccion', models.CharField(blank=True, max_length=1000, null=True)),
                ('direccion_atencion', models.CharField(blank=True, max_length=1000, null=True)),
                ('referencia', models.CharField(blank=True, max_length=1000, null=True)),
                ('comprobante', models.CharField(blank=True, max_length=1000, null=True)),
                ('boleta', models.BooleanField(default=True, max_length=1000)),
                ('factura', models.BooleanField(default=True, max_length=1000)),
                ('mismo_cliente', models.CharField(blank=True, max_length=1000, null=True)),
                ('nombre_boleta', models.CharField(blank=True, max_length=1000, null=True)),
                ('direccion1', models.CharField(blank=True, max_length=1000, null=True)),
                ('dni_c', models.CharField(blank=True, max_length=1000, null=True)),
                ('ruc', models.CharField(blank=True, max_length=1000, null=True)),
                ('razon_social', models.CharField(blank=True, max_length=1000, null=True)),
                ('direccion_rs', models.CharField(blank=True, max_length=1000, null=True)),
                ('pago', models.CharField(blank=True, max_length=1000, null=True)),
                ('correo', models.CharField(blank=True, max_length=1000, null=True)),
                ('atiende', models.CharField(blank=True, max_length=1000, null=True)),
                ('almacen', models.CharField(blank=True, max_length=1000, null=True)),
                ('gmail', models.FileField(upload_to='static')),
                ('status', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Estado')),
                ('observaciones', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
                ('modelo', models.CharField(blank=True, max_length=1000, null=True)),
                ('version', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='produccion',
            name='marca_vehiculo',
            field=models.ForeignKey(blank=True, help_text='Marca del veh\xedculo (p.e. Nissan)', max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_marca', to='app.Vehiculo'),
        ),
        migrations.AddField(
            model_name='produccion',
            name='modelo',
            field=models.ForeignKey(blank=True, help_text='Modelo del veh\xedculo ', max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_modelo', to='app.Vehiculo'),
        ),
    ]
