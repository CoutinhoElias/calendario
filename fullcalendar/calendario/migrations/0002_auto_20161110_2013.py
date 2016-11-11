# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaluo',
            fields=[
                ('avaluo_id', models.AutoField(primary_key=True, serialize=False)),
                ('referencia', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.AddField(
            model_name='evento',
            name='avaluo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calendario.Avaluo'),
        ),
    ]
