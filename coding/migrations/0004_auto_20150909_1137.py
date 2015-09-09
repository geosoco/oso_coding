# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0003_auto_20150831_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assigned_tweets',
            field=models.ManyToManyField(to='main.Tweet', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='assigned_users',
            field=models.ManyToManyField(to='main.User', null=True, blank=True),
        ),
    ]
