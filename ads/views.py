from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# I'll have to import the model functions
# Also create new from forms
# both of which I'll have to create first.
# from .models import ToDoList, Item # I'll rename these...
# from .forms import CreateNewAd


def index(response):
	return render(response, "ads/home.html", {})
# HttpResponse("Testing, 3..2..1")

def create(response):
        if response.method == "POST":
                form = CreateNewList(response.POST)
                if form.is_valid():
                        n = form.cleaned_data["name"]
                        t = ToDoList(name=n) # This variable needs a name change, creation, and import.
                        t.save()
                        response.user.todolist.add(t)
                return HttpResponseRedirect("/ads/%i" %t.id)
        else:
                form = CreateNewList()
        return render(response, "ads/create.html", {"form":form})
