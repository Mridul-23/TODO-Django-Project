
from django.contrib import admin
from django.urls import path
from .views import home, login, signup, add_todo, delete_todo, change_todo, signout
from django.conf.urls import handler404
from django.shortcuts import render


urlpatterns = [
    path("", home, name = 'home'),
    path("login", login, name = 'login'),
    path("signup", signup, name = 'signup'),
    path("logout", signout),
    path("add-todo", add_todo),
    path("delete-todo/<int:id>", delete_todo),
    path("change-status/<int:id>/<str:status>", change_todo)
]