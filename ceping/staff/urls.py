from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^staff.html$', 'staff.views.get_staffs', name='staff_get_staffs'),

)
