
from projects.models import Project
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound


def project_index(request):
    try:
        projects = Project.objects.all()
        context = {"projects": projects}
    except Project.DoesNotExist:
        return HttpResponseNotFound("Page not found")
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
        context = {"project": project}
    except Project.DoesNotExist:
        return HttpResponseNotFound("Page not found")
    return render(request, "project_detail.html", context)
