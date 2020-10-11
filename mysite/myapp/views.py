from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from . import models
from . import forms

# Create your views here.
def index(request):
    if request.method =="POST":
        suggestion_form = forms.SuggestionForm(request.POST)
        if suggestion_form.is_valid():
            suggestion_form.save(request)
            suggestion_form = forms.SuggestionForm()
    else:
        suggestion_form = forms.SuggestionForm()
    
    suggestion_objects = models.SuggestionModel.objects.all()
    suggestion_list = []
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(suggestion=sugg)
        temp_sugg = {}
        temp_sugg["suggestion"] = sugg.suggestion
        temp_sugg["id"] = sugg.id
        temp_sugg["author"] = sugg.author.username
        temp_sugg["comments"] = comment_objects
        suggestion_list+=[temp_sugg]

    context = {
        "title":"Suggestions",
        "suggestions":suggestion_list,
        "form":suggestion_form,
    }
    return render(request, "index.html", context=context)


def get_suggestions(request):
    suggestion_objects = models.SuggestionModel.objects.all()
    suggestion_list = {}
    suggestion_list["suggestions"]=[]
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(suggestion=sugg)
        temp_sugg = {}
        temp_sugg["suggestion"]=sugg.suggestion
        temp_sugg["author"]=sugg.author.username
        temp_sugg["id"]=sugg.id
        temp_sugg["comments"]=[]
        for comm in comment_objects:
            temp_comm={}
            temp_comm["comment"]=comm.comment
            temp_comm["id"]=comm.id
            temp_comm["author"]=comm.author.username
            temp_sugg["comments"]+=[temp_comm]
        suggestion_list["suggestions"]+=[temp_sugg]
    return JsonResponse(suggestion_list)


