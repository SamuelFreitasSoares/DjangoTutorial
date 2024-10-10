from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("Tech with Tim!")

def v1(response):
    return HttpResponse("V1")