from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<path>.+)/((?P<revision>[0-9a-f]{40}))/', 'wiki.views.view'),
    (r'^(?P<path>.+)/', 'wiki.views.view'),
    (r'^update_me!', 'wiki.updater.on_github_commit')
)
