from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView
from django.utils import timezone
from django.db.models import Count
from django.core import serializers
from django_genericfilters.views import FilteredListView
from forms import TweetListForm

import main.models as main_models


class HomeView(TemplateView):

	"""Home view."""

	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		return context


class UserListView(ListView):

	"""List of all users."""

	template_name = "users/list.html"
	paginate_by = 50

	def get_queryset(self):
		qs = main_models.User.objects.only(
				'id', 'screen_name', 'name', 'location').annotate(
				Count('tweet')
			).order_by(
				'-tweet__count')
		return qs

	def get_context_data(self, **kwargs):
		context = super(UserListView, self).get_context_data(**kwargs)
		return context


class UserDetailView(DetailView):
	model = main_models.User
	template_name = "users/detail.html"
	slug_field = 'screen_name'
	slug_url_kwarg = 'screen_name'
	query_pk_and_slug = True


class TweetListView(ListView):

	"""list all the tweets!"""

	template_name = "tweets/list.html"
	paginate_by = 50

	def get_queryset(self):
		qs = main_models.Tweet.objects.only(
				'id', 'user_screen_name', 'text', 'user__verified',
				'user__name', 'created_ts', 'retweet_count', 'favorite_count', 
				'retweeted_status_user_screen_name', 'retweeted_status__text' )
		return qs

	def get_context_data(self, **kwargs):
		context = super(TweetListView, self).get_context_data(**kwargs)
		return context


class TweetDetailView(DetailView):

	"""detail info for the Tweet."""

	model = main_models.Tweet
	template_name = "tweets/detail.html"




class TweetFilterListView(FilteredListView):
	"""filtered list."""
	model = main_models.Tweet
	template_name = "tweets/list.html"
	paginate_by = 10
	
	form_class = TweetListForm

	search_fields = ['user_screen_name', 'text', 'source']
	#filter_fields = ['lang', 'user_screen_name', 'created_ts', 'local_time', 'retweet_count', 'favorite_count']
	default_order = 'id'




