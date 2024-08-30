from django.shortcuts import render
from .models import Organization, Project, Skill, Honor, Course

# Create your views here.
def index(request):
    return render(request, 'index.html')

def education(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    honors = Honor.objects.all()
    courses = Course.objects.all()
    
    print("image url: ", projects[0].image.url)

    context = {
        'projects': projects,
        'skills': skills,
        'honors': honors,
        'courses': courses,
    }

    
    return render(request, 'education.html',context)