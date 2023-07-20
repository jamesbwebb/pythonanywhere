from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def learn(response):

	return render(response, "learnkana/learn.html", {})
