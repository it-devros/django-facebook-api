# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date

# Create your models here.


class Adaccount(models.Model):
  accountname = models.CharField(max_length=250)

  def __str__(self):
    return self.accountname

class Performance(models.Model):
  adaccount = models.ForeignKey(Adaccount, on_delete=models.CASCADE)
  date = models.DateField()
  campaign = models.CharField(max_length=500)
  adset = models.CharField(max_length=500)	
  spend = models.FloatField(blank=True, null=True)
  clicks = models.IntegerField()
  impressions = models.IntegerField()
  ctr = models.FloatField()
  cpc = models.FloatField()
  cpm = models.FloatField()
  conv1 = models.IntegerField()
  conv2 = models.IntegerField(blank=True, null=True)
  conv3 = models.IntegerField(blank=True, null=True)

  def __str__(self):
    return str(self.date) + ' - ' + str(self.adaccount)

  # Calculate cost per conversion of conv3
  def convtotal(self):
    try:
      convtotal = self.spend / self.conv3
    except ZeroDivisionError:
      convtotal = 0
    return convtotal

  # Calculate monthly ad spend
  def monthlyspend(self):
    currentMonth = datetime.now().month


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adaccounts = models.ForeignKey(Adaccount,null=True)
    company = models.CharField(max_length=250, blank=True)
    website = models.CharField(max_length=30, blank=True)

    def __str__(self):
    return self.company

@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    instance.account.save()
