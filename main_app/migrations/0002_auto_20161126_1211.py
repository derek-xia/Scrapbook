# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 20:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='picture',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
