# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-07 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

  dependencies = [
    ('dashboard', '0006_auto_20180107_1712'),
  ]

  operations = [
    migrations.AddField(
      model_name='account',
      name='adaccounts',
      field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Adaccount'),
    ),
  ]
