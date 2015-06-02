from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('officesupply.views',
                       url(r'^$', 'index', name='os_index'),
                       url(r'^sign$', 'sign', name='os_sign')

)
