# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GreatHomesRealty', '0002_auto_20161120_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='MLS',
            field=models.IntegerField(),
        ),
    ]
