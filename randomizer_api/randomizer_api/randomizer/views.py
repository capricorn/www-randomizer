from django.shortcuts import render
from django.http import HttpResponseRedirect 

def randomizer(request):
    return HttpResponseRedirect('https://google.com')