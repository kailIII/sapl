# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-29 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comissoes', '0007_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participacao',
            name='composicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participacao_set', to='comissoes.Composicao'),
        ),
    ]
