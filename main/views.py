# This code serves http requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def index(response, id):
# This is a database query using the id# passed into the url
	ls = ToDoList.objects.get(id=id)
	item = ls.item_set.get(id=1)

# for the HttpResponse object you can integrate html tags.
# This is pretty cool because we are returning the database object attribute!
	return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))

