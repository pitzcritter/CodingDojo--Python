# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-31 05:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userd', '0003_auto_20180130_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='cuser_id',
        ),
    ]
