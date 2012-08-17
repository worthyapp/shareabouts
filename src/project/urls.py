from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # For now, use basic auth.
    url(r'^accounts/', include('django.contrib.auth.urls')),

    # For now, the API and the management console are hosted together.
    url(r'^api/v1/', include('sa_api.urls')),
    url(r'^manage/', include('sa_manager.urls')),

)
