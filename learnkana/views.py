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
	passthrough['answer'] = kana.text
	passthrough['kana'] = kana.hir

	return render(response, "learnkana/learn.html", passthrough)
