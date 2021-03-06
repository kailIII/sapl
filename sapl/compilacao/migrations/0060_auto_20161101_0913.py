# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-01 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compilacao', '0059_auto_20161027_1323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dispositivo',
            options={'ordering': ['ta', 'ordem'], 'permissions': (('change_dispositivo_edicao_dinamica', 'Permissão de edição de dispositivos originais via editor dinâmico.'), ('change_dispositivo_edicao_avancada', 'Permissão de edição de dispositivos originais via formulários de edição avançada.'), ('change_dispositivo_registros_compilacao', 'Permissão de registro de compilação via editor dinâmico.'), ('view_dispositivo_notificacoes', 'Permissão de acesso às notificações de pendências.')), 'verbose_name': 'Dispositivo', 'verbose_name_plural': 'Dispositivos'},
        ),
    ]
