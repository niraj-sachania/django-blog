from django.shortcuts import render
from django.http import HttpResponse

def blog(response):
    return HttpResponse("Hello, blog!")