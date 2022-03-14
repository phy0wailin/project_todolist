from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse



# Create your views here.
def index(request):
    if not "tasks" in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def submit(request):
    if request.method == "POST":
        task = request.POST["task"]
        request.session["tasks"] += [task]
        return HttpResponseRedirect(reverse("tasks:index"))
    return render(request, "tasks/index.html")

def pop(request):
    request.session["tasks"] = []
    return HttpResponseRedirect(reverse("tasks:index"))
