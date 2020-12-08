from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

from django.views.generic import DeleteView
from django.http import Http404

from django.conf import settings

from . import models

def must_be_unique(value):
    user = User.objects.filter(email=value)
    if len(user) > 0:
        raise forms.ValidationError("Email Already Registered")
    return value

class SuggestionForm(forms.Form):
    suggestion = forms.CharField(
        label='Appointment',
        required=True,
        max_length=240,
    )
    date_input = forms.DateField(
        label='Date',
        widget=forms.DateInput(format='%m/%d/%Y'),
        input_formats=settings.DATE_INPUT_FORMATS,
    )
    time_input = forms.TimeField(
        label='Time',
        widget=forms.TimeInput(format='%H:%M'),
        input_formats=settings.TIME_INPUT_FORMATS,
    )

    def save(self, request):
        suggestion_instance = models.SuggestionModel()
        suggestion_instance.suggestion = self.cleaned_data["suggestion"]
        suggestion_instance.author = request.user
        suggestion_instance.date_input = self.cleaned_data["date_input"]
        suggestion_instance.time_input = self.cleaned_data["time_input"]

        suggestion_instance.save()
        return suggestion_instance


class CommentForms(forms.Form):
    comment= forms.CharField(
        label='Comment',
        required=True,
        max_length=240,
    )

    def save(self, request, sugg_id):
        suggestion_instance = models.SuggestionModel.objects.get(id=sugg_id)
        comment_instance = models.CommentModel()
        comment_instance.suggestion = suggestion_instance
        comment_instance.comment = self.cleaned_data["comment"]
        comment_instance.author = request.user
        comment_instance.save()
        return comment_instance


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[must_be_unique]
    )

    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

# class MyDeleteView(DeleteView):
#     def get_object(self, queryset=None):
#         obj = super(MyDeleteView, self).get_object()
#         if not obj.owner == self.request.user:
#             raise Http404
#         return obj