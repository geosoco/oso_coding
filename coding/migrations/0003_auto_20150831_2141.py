# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0002_auto_20150831_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='name',
            field=models.CharField(default='test', max_length=64),
            preserve_default=False,
        ),
    ]
