from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def test1(request, *args, **kwargs):
    return HttpResponseNotFound('<h1>Page not found</h1>')