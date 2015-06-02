from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^$', 'ceping.views.index', name='ceping_index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login.html$', 'ceping.views.logins', name='ceping_login'),
    url(r'^logout.html$', 'ceping.views.logouts', name='ceping_logouts'),
    url(r'^password.html$', 'ceping.views.password', name='ceping_password'),


    url(r'^admin/', include(admin.site.urls)),

    url(r'^poll/', include('poll.urls')),
    url(r'^staff/', include('staff.urls')),
    url(r'^officesupply/', include('officesupply.urls')),

)
