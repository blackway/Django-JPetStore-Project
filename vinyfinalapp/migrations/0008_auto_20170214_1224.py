# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-14 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinyfinalapp', '0007_auto_20170214_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinyitems',
            name='vprice',
            field=models.FloatField(default=0.0),
        ),
    ]
