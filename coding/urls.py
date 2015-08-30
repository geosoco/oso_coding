from django.conf.urls import patterns, url
from coding.views import *

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
)
