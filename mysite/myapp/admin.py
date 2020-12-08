from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from . import models

# Register your models here.
admin.site.register(models.SuggestionModel)
admin.site.register(models.CommentModel)
