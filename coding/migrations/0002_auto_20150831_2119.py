# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('coding', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='user',
            new_name='coder',
        ),
        migrations.AddField(
            model_name='assignment',
            name='assigned_tweets',
            field=models.ManyToManyField(to='main.Tweet'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='assigned_users',
            field=models.ManyToManyField(to='main.User'),
        ),
    ]
