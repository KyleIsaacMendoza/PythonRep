from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name='index'), #use index function in views.py
     path('login', views.login_view, name='login'), #use login_view function in views.py
     path('logout', views.logout_view, name="logout")
]