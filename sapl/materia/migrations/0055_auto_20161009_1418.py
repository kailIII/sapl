# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-09 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_auto_20161009_1222'),
        ('materia', '0054_auto_20161009_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialegislativa',
            name='autores',
            field=models.ManyToManyField(through='materia.Autoria', to='base.Autor'),
        ),
        migrations.AlterField(
            model_name='autoria',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Autor', verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='autoria',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materia.MateriaLegislativa', verbose_name='Matéria Legislativa'),
        ),
    ]
