from django.conf.urls.defaults import *
from django.contrib import admin
from views import home, blog
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', home), # let home display the four most recent posts
    (r'^admin/(.*)', admin.site.root),
    (r'^blog/(?P<year>[\w\._-]+)/$', 'blog', name='year'),
    (r'^blog/(?P<month>[\w\._-]+)/(?P<year>[\w\._-]+)/$', 'blog', name='month'),
    (r'^blog/(?P<day>[\w\._-]+)/(?P<year>[\w\._-]+)/(?P<year>[\w\._-]+)/$', 'blog', name='day'),
)
