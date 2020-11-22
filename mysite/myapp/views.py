from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.http import HttpResponse


def homepage_view(request):
    return render(request, 'hello_world.html', {})

