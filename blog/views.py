from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_blog(request):
    return HttpResponse("Hello, Blog!")