# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wifimanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ip_addr',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(default='not set', max_length=200),
        ),
    ]
