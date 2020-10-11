from django import forms

from . import models

class SuggestionForm(forms.Form):
    suggestion = forms.CharField(
        label='Suggestion',
        required=True,
        max_length=240,
    )

    def save(self, request):
        suggestion_instance = models.SuggestionModel()
        suggestion_instance.suggestion = self.cleaned_data["suggestion"]
        suggestion_instance.author = request.user
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
