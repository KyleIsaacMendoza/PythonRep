from django.shortcuts import render


from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout 
#for login, logout and authenticate

# Create your views here.

def index(request):
    #if not authenticated go to login view
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        #autheticate this user's user and pass if it is existing and correct
        user = authenticate(request, username=username, password=password)
        
        #if correct
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))   
        else:
            #if wrong
            #redirect to same page and show a message 
            return render(request, "users/login.html", {
                "message": "Invalid Credentials" #the message
            })
        
    return render(request, "users/login.html")

def logout_view(request):
    #to logout
    logout(request)
    #return to login page and say a message that you just logged out
    return render(request, "users/login.html", {
        "message": "Logged Out."
    })