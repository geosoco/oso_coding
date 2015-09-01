from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView
import models as coding_models
import forms as coding_forms
import main.models as main_models
from django.utils.timezone import now

class HomeView(ListView):

    """Home view."""

    template_name = "coding/assignments.html"

    def get_queryset(self):
        qs = coding_models.Assignment.objects.filter(
            coder=self.request.user)
        return qs


    #def get_context_data(self, **kwargs):
    #    context = super(HomeView, self).get_context_data(**kwargs)
    #    return context


class UserView(TemplateView):
    """
    User View.
    """

    template_name = "coding/users/detail.html"


class CodingView(TemplateView):
    """
    Coding View.
    """

    template_name = "coding/assignments/index.html"


class CreateAssignmentView(CreateView):
    """
    Create AssignmentView
    """

    model = coding_models.Assignment
    template_name = "coding/assignment.create.html"
    form_class = coding_forms.AssignmentCreationForm
    success_url = "/coding/assignment/create/"

    def form_valid(self, form):
        """ handle the form properly."""

        # assigned user ids
        assigned_users = None
        user_ids_text = form.cleaned_data["user_ids"]
        if user_ids_text:
            user_ids = [int(id.strip()) for id in user_ids_text.split(',')]


            assigned_users = main_models.User.objects.filter(
                pk__in=user_ids)
            form.cleaned_data["assigned_users"] = assigned_users


        # save the form
        self.object = form.save(commit=False)
        # assigned creation
        self.object.created_by = self.request.user
        self.created_date = now()

        # save data so that we can add all the assigned users
        self.object.save()
        self.object.assigned_users.add(*assigned_users)
        form.save_m2m()


        return super(CreateAssignmentView, self).form_valid(form)

