# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170402_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50, verbose_name='课程名字'),
        ),
    ]
