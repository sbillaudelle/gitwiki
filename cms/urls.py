from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^update', 'cms.updater.update'),
    (r'^(?P<path>.+)/((?P<revision>[0-9a-f]{40}))', 'cms.views.view'),
    (r'^(?P<path>.*)', 'cms.views.view'),
    (r'', 'django.views.defaults.page_not_found')
)
