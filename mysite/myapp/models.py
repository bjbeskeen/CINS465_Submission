from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.forms import TextInput, Textarea



# Create your models here.
class SuggestionModel(models.Model):
    suggestion = models.CharField(max_length=240)
    # author = models.ForeignKey(User, on_delete=models.CASCADE) #new
    date_input = models.DateField(null=True)
    time_input = models.TimeField(null=True)

    def __str__(self):
        return self.suggestion

class CommentModel(models.Model):
    comment = models.CharField(max_length=240) #new
    author = models.ForeignKey(User, on_delete=models.CASCADE) #new
    suggestion = models.ForeignKey(SuggestionModel, on_delete=models.CASCADE)

    def __str__(self): #new
        return self.comment
