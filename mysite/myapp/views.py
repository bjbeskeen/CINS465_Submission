from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


from . import models
from . import forms

# Create your views here.
@login_required
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

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
        context = {
            "form":form_instance,
        }
        return render(request, "registration/registration.html", context=context)

def logout_view(request):
    logout(request)
    return redirect("/login/")




# NEWER GET_SUGGESTIONS CODE
# suggestion_objects = models.SuggestionModel.objects.all().order_by('-published_on')
#     suggestion_list = {}
#     suggestion_list["suggestions"]=[]
#     for sugg in suggestion_objects:
#         comment_objects = models.CommentModel.objects.filter(suggestion=sugg).order_by('published_on')
#         temp_sugg = {}
#         temp_sugg["suggestion"]=sugg.suggestion
#         temp_sugg["author"]=sugg.author.username
#         temp_sugg["id"]=sugg.id
#         temp_sugg["date"]=sugg.published_on.strftime("%Y-%m-%d %H:%M:%S")
#         if sugg.image:
#             temp_sugg["image"]=sugg.image.url
#             temp_sugg["image_desc"]=sugg.image_description
#         else:
#             temp_sugg["image"]=""
#             temp_sugg["image_desc"]=""
#         temp_sugg["comments"]=[]
#         for comm in comment_objects:
#             temp_comm={}
#             temp_comm["comment"]=comm.comment
#             temp_comm["id"]=comm.id
#             temp_comm["author"]=comm.author.username
#             time_diff = datetime.now(timezone.utc) - comm.published_on
#             time_diff_s = time_diff.total_seconds()
#             if time_diff_s < 60:
#                 temp_comm["date"] = "published " + str(int(time_diff_s)) + " seconds ago"
#             else:
#                 time_diff_m = divmod(time_diff_s, 60)[0]
#                 if time_diff_m < 60:
#                     temp_comm["date"] = "published " + str(int(time_diff_m)) + " minutes ago"
#                 else:
#                     time_diff_h = divmod(time_diff_m, 60)[0]
#                     if time_diff_h < 24:
#                         temp_comm["date"] = "published " + str(int(time_diff_h)) + " hour ago"
#                     else:
#                         temp_comm["date"]  = "published on " + comm.published_on.strftime("%Y-%m-%d")
#             temp_sugg["comments"]+=[temp_comm]
#         suggestion_list["suggestions"]+=[temp_sugg]
#     return JsonResponse(suggestion_list)
