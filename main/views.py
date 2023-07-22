# This code serves http requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

def index(response, id):
# This is a database query using the id# passed into the url
	ls = ToDoList.objects.get(id=id)
	if ls in response.user.todolist.all():
		if response.method == "POST":
	# This checks to see which button was clicked to init the post request
			if response.POST.get("save"):
				for item in ls.item_set.all():
	# This checks the value of all check boxes and saves it into our database
					if response.POST.get("c" + str(item.id)) == "clicked":
						item.complete = True
					else:
						item.complete = False
					item.save()
	# Here we take the text from the entry box and create an incomplete ToDoList item.
			elif response.POST.get("newItem"):
				txt = response.POST.get("new")
				if len(txt) > 2:
					ls.item_set.create(text=txt, complete=False)
				else:
	# This could be made more robust by adding something to validate the input.
					print("invalid")

	# for the HttpResponse object you can integrate html tags.
	# This is pretty cool because we are returning the database object attribute!
		return render(response, "main/list.html", {"ls":ls})
	return render(response, "view.html", {})
def home(response):
	return render(response, "main/home.html", {})

def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)
		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()
			response.user.todolist.add(t)
		return HttpResponseRedirect("/view/")
#		return HttpResponseRedirect("/main/%i" %t.id)
	else:
		form = CreateNewList()


	return render(response, "main/create.html", {"form":form})

def view(response):

	return render(response, "main/view.html", {})

