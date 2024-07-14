from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string

def index(request):
    rendered = render_to_string("index.html", {"foo": "bar"})
    return HttpResponse(rendered)

def store(request):
    rendered = render_to_string("store.html", {"foo": "bar"})
    return HttpResponse(rendered)

def rating(request):
    rendered = render_to_string("rating.html", {"foo": "bar"})
    return HttpResponse(rendered)

def profile(request):
    rendered = render_to_string("profile.html", {"foo": "bar"})
    return HttpResponse(rendered)
