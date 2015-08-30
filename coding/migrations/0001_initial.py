# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='assignment_created_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', models.ForeignKey(related_name='assignment_deleted_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='assignment_modified_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(null=True, blank=True)),
                ('css_class', models.CharField(max_length=64, null=True, blank=True)),
                ('key', models.CharField(max_length=1, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='code_created_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', models.ForeignKey(related_name='code_deleted_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='code_modified_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CodeScheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('mutually_exclusive', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(related_name='codescheme_created_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', models.ForeignKey(related_name='codescheme_deleted_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='codescheme_modified_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TweetCodeInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('assignment', models.ForeignKey(blank=True, to='coding.Assignment', null=True)),
                ('code', models.ForeignKey(to='coding.Code')),
                ('created_by', models.ForeignKey(related_name='tweetcodeinstance_created_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', models.ForeignKey(related_name='tweetcodeinstance_deleted_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='tweetcodeinstance_modified_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('tweet', models.ForeignKey(to='main.Tweet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserCodeInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('assignment', models.ForeignKey(blank=True, to='coding.Assignment', null=True)),
                ('code', models.ForeignKey(to='coding.Code')),
                ('created_by', models.ForeignKey(related_name='usercodeinstance_created_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', models.ForeignKey(related_name='usercodeinstance_deleted_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='usercodeinstance_modified_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(to='main.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='code',
            name='scheme',
            field=models.ForeignKey(to='coding.CodeScheme'),
        ),
    ]
