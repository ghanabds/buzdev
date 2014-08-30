from Service_providers import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='home'),

)