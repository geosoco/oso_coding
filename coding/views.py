from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView

class HomeView(TemplateView):

    """Home view."""

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context