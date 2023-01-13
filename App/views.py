from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Wish(requrst,name):
    return HttpResponse(f'<h1>Good Afternoon {name} Sir</h1>')