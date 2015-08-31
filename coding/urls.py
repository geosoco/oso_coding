from django.conf.urls import patterns, url
from coding.views import *

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^user/$', UserView.as_view(), name='coding-user'),
)
