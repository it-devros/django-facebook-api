# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-10 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

  dependencies = [
    ('dashboard', '0007_account_adaccounts'),
  ]

  operations = [
    migrations.AddField(
      model_name='performance',
      name='spend',
      field=models.FloatField(blank=True, null=True),
    ),
    migrations.AlterField(
      model_name='performance',
      name='date',
      field=models.DateField(auto_now_add=True),
    ),
  ]
