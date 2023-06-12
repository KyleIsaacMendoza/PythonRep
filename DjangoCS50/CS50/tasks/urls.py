from django.urls import path

from . import views

app_name = "tasks"
 #to be unique and no name collision between apps
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]