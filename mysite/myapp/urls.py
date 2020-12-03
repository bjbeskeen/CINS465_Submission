from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index),
    path('login/', auth_views.LoginView.as_view()),
    path('suggestions/', views.get_suggestions),
    path('home/', views.index),
    path('register/', views.register),
    path('logout/', views.logout_view),

]