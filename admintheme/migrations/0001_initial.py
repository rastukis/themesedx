# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('main_color', models.CharField(max_length=6)),
                ('dark_color', models.CharField(max_length=6)),
                ('light_color', models.CharField(max_length=6)),
                ('bg_color', models.CharField(max_length=6)),
                ('main_bg', models.CharField(max_length=6)),
                ('secondary', models.CharField(max_length=6)),
                ('gray', models.CharField(max_length=6)),
                ('gray_3', models.CharField(max_length=6)),
                ('gray_2', models.CharField(max_length=6)),
                ('gray_1', models.CharField(max_length=6)),
                ('black', models.CharField(max_length=6)),
                ('black_80', models.CharField(max_length=6)),
                ('logo_header', models.CharField(max_length=250)),
                ('banner', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_log', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=250)),
                ('User', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='changelog',
            name='Instance',
            field=models.ForeignKey(to='admintheme.Instance'),
        ),
        migrations.AddField(
            model_name='attributes',
            name='Instance',
            field=models.ForeignKey(to='admintheme.Instance'),
        ),
    ]
