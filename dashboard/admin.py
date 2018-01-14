# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Adaccount, Account, Performance

# Register your models here.

admin.site.register(Adaccount)
admin.site.register(Account)
admin.site.register(Performance)