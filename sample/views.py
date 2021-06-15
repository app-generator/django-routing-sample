from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 
from random import random
import requests

def hello(request): 
    return HttpResponse("Hello Django") 

def myrandom(request): 
    return HttpResponse("Random - " + str( random() ) ) 

def randomimage(request):
    r = requests.get('http://thecatapi.com/api/images/get?format=src&type=png')
    return HttpResponse( r.content, content_type="image/png")
