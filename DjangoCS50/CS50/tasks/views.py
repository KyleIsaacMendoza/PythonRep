from django import forms #needed to use forms.Form
from django.shortcuts import render
from django.http import HttpResponseRedirect #redirect
from django.urls import reverse
# Create your views here.



#to add form instead of making in HTML
class NewTaskForm(forms.Form): 
    #forms is imported and .Form is the function
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value =1, max_value=5)




def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
        # key : value
        # key - what is the variable that html is accessing to
        # value = is the variable/values inside the views.py
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST) 
        #request.POST contains all the data that the user submitted
        
        if form.is_valid():
           
           #take data from the form, get the task, save it in variable task
           task = form.cleaned_data["task"]
           
           request.session["tasks"] += [task]
           # append to the list of tasks that already form
           
           #redirect to index after submitting
           return HttpResponseRedirect(reverse("tasks:index"))
        
        else: 
            return render(request, "tasks/add.html", {
                "form": form
            })
        
    return render(request, "tasks/add.html", {
        "form": NewTaskForm() #class u make
    })
