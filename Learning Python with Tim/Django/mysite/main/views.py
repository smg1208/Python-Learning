from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<h1> tech with me!</h1>")

def V1(response):
    return HttpResponse("<h1> View 1! </h1>")