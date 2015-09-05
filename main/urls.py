from django.conf.urls import patterns, url
import main.views as main_views

urlpatterns = patterns(
    '',
    url(r'^$', main_views.HomeView.as_view(), name='home'),
    url(r'^users/$', main_views.UserListView.as_view(), name='users-list'),
    url(r'^users/((?P<pk>[0-9]+)|(?P<screen_name>\w+))/$',
        main_views.UserDetailView.as_view(), name='user-detail'),
    url(r'^tweets/$', main_views.TweetListView.as_view(), name='tweets-list'),
    url(r'^tweets/search/$', main_views.TweetFilterListView.as_view(),
        name='tweets-search'),
    url(r'^tweets/(?P<pk>[0-9]+)/$', main_views.TweetDetailView.as_view(),
        name='tweet-detail'),
    url(r'^hashtags/$', main_views.HashtagListView.as_view(),
        name='hashtag-list'),
    url(r'^urls/$', main_views.HomeView.as_view(), name='urls-list'),
    url(r'^media/$', main_views.HomeView.as_view(), name='media-list'),
    url(r'^codes/$', main_views.HomeView.as_view(), name='codes-list'),
)
