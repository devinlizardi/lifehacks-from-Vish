# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hometown',
            field=models.CharField(max_length=25),
        ),
    ]