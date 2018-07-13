# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-11 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vegetables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('cost', models.IntegerField()),
            ],
            options={
                'db_table': 'vegetables',
            },
        ),
    ]
