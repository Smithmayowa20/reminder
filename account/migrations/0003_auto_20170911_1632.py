# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-11 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20170911_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
