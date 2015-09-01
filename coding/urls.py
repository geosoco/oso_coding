from django.conf.urls import patterns, url
from coding.views import *

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^user/$', UserView.as_view(), name='coding-user'),
    url(r'^assignment/create/$', CreateAssignmentView.as_view(), name='coding-assignment-create'),
    url(r'^assignment/$', CodingView.as_view(), name='coding-assignment'),
)
