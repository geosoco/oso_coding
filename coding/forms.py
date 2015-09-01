from django import forms
import models as coding_models

class AssignmentCreationForm(forms.ModelForm):
    user_ids = forms.CharField(
        widget=forms.Textarea,
        help_text="a comma separated list of ids",
        required=False)
    #tweet_ids = forms.CharField(
    #    widget=forms.Textarea,
    #    help_text="a comma separated list of ids",
    #    required=False)


    class Meta:
        model = coding_models.Assignment
        fields = ['name', 'description', 'coder']
