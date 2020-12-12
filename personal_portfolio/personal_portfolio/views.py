from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required


# Webpage that is only viewable in login mode
@login_required
def hello(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)


def get_about(request):
    return render(request, "about.html")


def get_members(request):
    return render(request, "members.html")