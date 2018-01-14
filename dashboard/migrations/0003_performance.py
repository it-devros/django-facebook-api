# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-07 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adaccount', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('campaign', models.CharField(max_length=500)),
                ('adset', models.CharField(max_length=500)),
                ('clicks', models.IntegerField()),
                ('impressions', models.IntegerField()),
                ('ctr', models.IntegerField()),
                ('cpc', models.IntegerField()),
                ('cpm', models.IntegerField()),
                ('conv1', models.IntegerField()),
            ],
        ),
    ]
