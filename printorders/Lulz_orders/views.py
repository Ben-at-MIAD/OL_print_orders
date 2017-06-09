from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This will be the place where student can order their prints")

# Create your views here.
