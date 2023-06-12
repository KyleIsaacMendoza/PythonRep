from django.urls import path #import url

#to use views
from . import views # . -> in the same directory

urlpatterns = [
    path("", views.index, name="index"), 
    #index is the function (dont forget the comma ,)
    
    path("<str:name>", views.greet, name="greet"), 
    # <str:name> specify any name
    #  more flexible type of greeting
    
    path("brian", views.brian, name="brian"),
    #http://127.0.0.1:8000/hello/brian
    
    path("david", views.david, name="david")
    #http://127.0.0.1:8000/hello/david
]