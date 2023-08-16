from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "ads/Ad_list.html"
class AdDetailView(OwnerDetailView):
    model = Ad
class AdCreateView(OwnerCreateView):
    model = Ad
    # List the fields to copy from the Ad model to the Ad form
    fields = ['title', 'price', 'text']
class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    # This would make more sense
    # fields_exclude = ['owner', 'created_at', 'updated_at']
class AdDeleteView(OwnerDeleteView):
    model = Ad


#from django.shortcuts import render
#from django.http import HttpResponse, HttpResponseRedirect
# I'll have to import the model functions
# Also create new from forms
# both of which I'll have to create first.
# from .models import ToDoList, Item # I'll rename these...
# from .forms import CreateNewAd


#def home(response):
#	return render(response, "ads/home.html", {})
# HttpResponse("Testing, 3..2..1")

#def create(response):
#        if response.method == "POST":
#                form = CreateNewList(response.POST)
#                if form.is_valid():
#                        n = form.cleaned_data["name"]
#                        t = ToDoList(name=n) # This variable needs a name change, creation, and import.
#                        t.save()
#                        response.user.todolist.add(t)
#                return HttpResponseRedirect("/ads/%i" %t.id)
#        else:
#                form = CreateNewList()
#	return render(response, "ads/create.html", {})
#        return render(response, "ads/create.html", {})

#def view(response):

#	return render(response, "ads/view.html", {})
