from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import KanaCheck
from .forms import KanaChecker
import random

# Create your views here.

def learn(response):
	passthrough = {}
	lk = KanaCheck.objects.all()
	kana = random.choice(lk)
	passthrough["answer"] = kana.text
	passthrough["kana"] = kana.hir
#	if response.method == "POST":
	form = KanaChecker(response.POST)
	passthrough["form"] = form
	if form.is_valid():
# Problem statement: Before compairing the guess to the answer the page reloads, this is a problem because it rerandomizes the answer.
		answer = passthrough["answer"]
		guess = form.cleaned_data["guess"].upper()
		if answer == guess:
			return HttpResponseRedirect("/create/")
		else:
			return HttpResponseRedirect("/view/{}".format(guess))

	return render(response, "learnkana/learn.html", passthrough)

# I'm thinking next time I'll try moving the top block of code into the if statement?
# another thing to try is go into the HTML file and make sure the action is disabled?
# I'm not sure if you can do that but I have the page reloading when I don't want to and the 'action' tag does that.
