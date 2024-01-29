"""Whenever we create a new page, we will ad that url in this urlpatterns"""
from django.urls import path
from . import views

urlpatterns=[
    path(route="", view=views.home, name="home"),
    path(route="login/", view=views.login_user, name="login_user"),
    path(route="logout/", view=views.logout_user, name="logout_user"),
    path(route="signup/", view=views.signup_user, name="signup_user"),
]