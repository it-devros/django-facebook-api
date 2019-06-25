from django.conf.urls import url
from . import views


urlpatterns = [

  # /dashboard/
  url(r'^$', views.IndexView.as_view(), name='index'),

  # filtering by date range picker
  url(r'filterBydate/(?P<startDate>\d{4}-\d{2}-\d{2})/(?P<endDate>\d{4}-\d{2}-\d{2})', views.FilterByDate.as_view(), name="filter_by_date"),

  # account page
  url(r'account/$', views.AccountView.as_view(), name='account'),

]