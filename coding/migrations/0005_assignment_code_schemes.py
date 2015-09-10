# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0004_auto_20150909_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='code_schemes',
            field=models.ManyToManyField(to='coding.CodeScheme'),
        ),
    ]
