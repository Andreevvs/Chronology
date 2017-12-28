# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_text', models.TextField()),
                ('article_data', models.DateTimeField()),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]