# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-31 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GreatHomesRealty', '0012_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='url',
            field=models.CharField(max_length=128, null=True),
        ),
    ]