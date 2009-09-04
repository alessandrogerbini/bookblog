from django.conf.urls.defaults import *
from django.contrib import admin
from views import home, YearArchive, MonthArchive, ByDay
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', home), # later, this will display the four most recent posts
    (r'^admin/(.*)', admin.site.root),
    # the patterns below match user input after 'blog/' for a date in the form of
        # yy/mm/dd
    (r'^blog/(?P<year>\d{4})/$', 'YearArchive'),
    (r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/$', 'MonthArchive'),
    (r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$', 'ByDay'),
    #(r'^blog/(?P<year>[\w\._-]+)/$', 'blog', name='year'),
    #(r'^blog/(?P<year>[\w\._-]+)/(?P<month>[\w\._-]+)/$', 'blog', name='month'),
    #(r'^blog/(?P<year>[\w\._-]+)/(?P<month>[\w\._-]+)/(?P<day>[\w\._-]+)/$', 'blog', name='day'),
)

    