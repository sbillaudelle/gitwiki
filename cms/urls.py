from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^update', 'cream.cms.updater.update'),
    (r'^(?P<path>.+)/((?P<revision>[0-9a-f]{40}))', 'cream.cms.views.view'),
    (r'^(?P<path>.*)', 'cream.cms.views.view'),
    (r'', 'django.views.defaults.page_not_found')
)
