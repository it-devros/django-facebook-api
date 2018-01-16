# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Account, Adaccount, Performance

from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adsinsights import AdsInsights
from facebookads.api import FacebookAdsApi

from datetime import datetime

# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView): 
	'''
	Get all performance for the logged in user
	'''
	model = Performance
	context_object_name = 'all_performance'
	template_name = 'dashboard/index.html'
	login_url = '/login/'
	redirect_field_name = 'redirect_to'

	def get_queryset(self):
		user = self.request.user
		adaccount_list = Account.objects.filter(user=user).values_list('adaccounts', flat=True)
		return Performance.objects.filter(adaccount__in=adaccount_list)


	# FB API Test
	access_token = 'EAAKXCZCXGv4QBALNsm5JM68GREQALlZCjU0ccUymdBlZCOoS7aa8QUV7mBh1meQjrbWsoi3NaFuMAYT3UowcD2QXjphE43pOynTeCPeQZADxepzZCg9NWQKV6XYKFnOFi9gInj213HUbZCOxirPOGXHXQDgHwi79cHhl0hL2Uf0BRj1ZAMGA0RE8VfnZBl87H65bONkX3OiZAwm3oPx8a0w1k'
	ad_account_id = 'act_116715782407326'
	app_secret = '20ab1bf0c4d6abb440e4dc17ab22e309'
	app_id = '729027577298820'
	FacebookAdsApi.init(access_token=access_token)

	fields = [
	    'campaign_name',
	    'clicks',
	    'cpc',
	    'ctr',
	]
	params = {
	    'level': 'adset',
	    'breakdowns': [],
	    'time_range': {'since':'2018-01-01','until':'2018-01-11'},
	}
	fb_data = AdAccount(ad_account_id).get_insights(
	    fields=fields,
	    params=params,
	)


class HomeView(TemplateView):
	model = Adaccount
	template_name = 'dashboard/home.html'


class AccountView(TemplateView):
	model = Adaccount
	template_name = 'dashboard/account.html'


# filtering the performance by date
class FilterByDate(generic.ListView):
	model = Performance
	context_object_name = 'filtered_performance'
	template_name = 'dashboard/filter.html'

	def get_queryset(self):
		user = self.request.user
		startDate = self.kwargs['startDate']
		endDate = self.kwargs['endDate']
		start_Date = datetime.now()
		end_Date = datetime.now()
		try:
			start_Date = datetime.strptime(startDate, '%Y-%m-%d')
			end_Date = datetime.strptime(endDate, '%Y-%m-%d')
			start_Date = datetime.date(start_Date)
			end_Date = datetime.date(end_Date)
		except Exception as e:
			print "Date validation error"
			return e
		adaccount_list = Account.objects.filter(user=user).values_list('adaccounts', flat=True)
		return Performance.objects.filter(adaccount__in=adaccount_list, date__range=(start_Date, end_Date))
