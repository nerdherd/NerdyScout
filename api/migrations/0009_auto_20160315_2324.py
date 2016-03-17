# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_team_teamname'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='alliance',
            field=models.CharField(choices=[('R', 'Red'), ('B', 'Blue')], default='R', max_length=1),
        ),
        migrations.AddField(
            model_name='match',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]