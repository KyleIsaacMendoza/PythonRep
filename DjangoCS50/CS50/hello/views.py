from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html") 
    #to render a entire html file

def brian(request):
    return HttpResponse("Hello, Brian")

def david(request):
    return HttpResponse("Hello, David")

def greet(request, name):
    return render(request, "hello/greet.html", {
        
        #third argument or called the context (optional)
        
        # all the information, variables, you want the template to access to
        
        "name": name.capitalize() #dictionary
    })
    # return HttpResponse(f"Hello, {name.capitalize()}")
    # str.capitalize() -> to capitalize first letter 
    # kyle -> Kyle