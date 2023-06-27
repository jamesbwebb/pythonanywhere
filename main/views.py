# This code serves http requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def index(response, id):
# This is a database query using the id# passed into the url
	ls = ToDoList.objects.get(id=id)

# for the HttpResponse object you can integrate html tags.
# This is pretty cool because we are returning the database object attribute!
	return render(response, "main/base.html", {"ls"=ls})

def home(response):

	return render(response, "main/home.html", {})
