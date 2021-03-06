# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-16 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpareParts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spoiler', models.IntegerField()),
                ('wheels', models.IntegerField()),
                ('brakes', models.IntegerField()),
                ('headlamps', models.IntegerField()),
                ('taillamps', models.IntegerField()),
                ('airbags', models.IntegerField()),
                ('clutchplates', models.IntegerField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cmodel', to='testapp.CarModels')),
            ],
        ),
    ]
