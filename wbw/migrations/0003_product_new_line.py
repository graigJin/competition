# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wbw', '0002_auto_20170327_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_line',
            field=models.BooleanField(default=False),
        ),
    ]