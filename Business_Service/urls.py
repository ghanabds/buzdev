from Business_Service import settings
from django.conf.urls import patterns, include, url
from Service_providers import urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Business_Service.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',"Service_providers.views.index"),
    url(r'^users/', include('Service_providers.urls'),),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )