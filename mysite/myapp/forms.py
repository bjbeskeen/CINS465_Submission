from django import forms
#from django.core.validators import validate_slug

from . import models

class SuggestionForm(forms.Form):
    suggestion = forms.CharField(
        label='Suggestion',
        required=True,
        max_length=240,
        #validators=[validate_slug],
    )

    def save(self):
        suggestion_instance = models.SuggestionModel()
        suggestion_instance.suggestion = self.cleaned_data["suggestion"]
        suggestion_instance.save()
        return suggestion_instance