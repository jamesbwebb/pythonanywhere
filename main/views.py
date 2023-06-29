# This code serves http requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

def index(response, id):
# This is a database query using the id# passed into the url
	ls = ToDoList.objects.get(id=id)
# for the HttpResponse object you can integrate html tags.
# This is pretty cool because we are returning the database object attribute!
	return render(response, "main/list.html", {"ls":ls})

def home(response):
	return render(response, "main/home.html", {})

def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()
		return HttpResponseRedirect("/main/%i" %t.id)
	else:
		form = CreateNewList()


	return render(response, "main/create.html", {"form":form})

