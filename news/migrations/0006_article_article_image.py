# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-01 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='default.png', upload_to='articles/'),
        ),
    ]