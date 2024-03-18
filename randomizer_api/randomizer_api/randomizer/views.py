from random import randint

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseServerError

from randomizer_api import settings

def randomizer(request):
    urls = settings.RANDOMIZER_URL_LIST
    if urls == []:
        return HttpResponseServerError('The URL list is empty.')

    url = urls[randint(0, len(urls)-1)]
    return HttpResponseRedirect(url)