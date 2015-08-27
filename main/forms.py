from django import forms
from django.utils.translation import ugettext_lazy as _
from django_genericfilters import forms as gf


class TweetListForm( gf.FilteredForm):
	def get_order_by_choices(self):
		return [('created_ts', _(u'date')),]