from django.shortcuts import render
from django.http import HttpResponse

def index(response):
	return HttpResponse("Testing, 3..2..1")
