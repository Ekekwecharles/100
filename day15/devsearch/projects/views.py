from django.shortcuts import render
from .models import Project

# Create your views here.

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    context = {
        'project': projectobj,
        'tags': tags,
    }
    return render(request, 'projects/single_project.html', context)