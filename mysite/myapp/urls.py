from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.views.i18n import JavaScriptCatalog

from . import views
from chat import views as chat_view

urlpatterns = [
    path('', views.index),
    # path('login/', auth_views.LoginView.as_view()),
    path('suggestions/', views.get_suggestions),
    path('register/', views.register),
    # path('logout/', views.logout_view), 
    path('jsi18n/', JavaScriptCatalog.as_view(), name='js-catalog'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('chat/', chat_view.index)
]