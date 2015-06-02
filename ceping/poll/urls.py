from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'poll.views.index', name='poll_index'),
    url(r'^best.html$', 'poll.views.best', name='poll_best'),
    url(r'^staff.html$', 'poll.views.staff', name='poll_staff'),
    url(r'^evaluation.html$', 'poll.views.evaluation', name='poll_evaluation'),



)
