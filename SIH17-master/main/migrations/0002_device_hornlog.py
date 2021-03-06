# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-01 03:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceID', models.CharField(default='', max_length=10)),
                ('aadhar', models.CharField(default='', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='HornLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(default='', max_length=20)),
                ('location_x', models.CharField(default='', max_length=20)),
                ('location_y', models.CharField(default='', max_length=20)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Device')),
            ],
        ),
    ]
