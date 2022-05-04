from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('profile', views.profile, name="profile"),
]