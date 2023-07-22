from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import KanaCheck
from .forms import KanaChecker


# Create your views here.

def learn(response):
	lk = KanaCheck.objects.all()

	return render(response, "learnkana/learn.html", {'lk':lk})
