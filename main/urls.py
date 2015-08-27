from django.conf.urls import patterns, url, include
from django.conf import settings

from main.views import *

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^users/$', UserListView.as_view(), name='users-list'),
	url(r'^users/((?P<pk>[0-9]+)|(?P<screen_name>\w+))/$', UserDetailView.as_view(), name='user-detail'),
	url(r'^tweets/$', TweetListView.as_view(), name='tweets-list'),
	url(r'^tweets/search/$', TweetFilterListView.as_view(), name='tweets-search'),
	url(r'^tweets/(?P<pk>[0-9]+)/$', TweetDetailView.as_view(), name='tweet-detail'),
	url(r'^urls/$', HomeView.as_view(), name='urls-list'),
	url(r'^media/$', HomeView.as_view(), name='media-list'),
	url(r'^codes/$', HomeView.as_view(), name='codes-list'),
)

