# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20170830_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]