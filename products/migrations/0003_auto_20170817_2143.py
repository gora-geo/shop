# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 17:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='short_description',
        ),
    ]
