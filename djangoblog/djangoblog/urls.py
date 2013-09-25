from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django_markdown import flatpages

admin.autodiscover()
flatpages.register()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoblog.views.home', name='home'),
    # url(r'^djangoblog/', include('djangoblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^blog/', include('blog.urls')),
    #url(r'^search/', include('haystack.urls')),
)
