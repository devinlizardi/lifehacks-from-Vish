# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wisdom',
            name='title',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]