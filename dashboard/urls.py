from django.conf.urls import url
from . import views


urlpatterns = [

	# /dashboard/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # account page
    url(r'account/$', views.AccountView.as_view(), name='account'),

]